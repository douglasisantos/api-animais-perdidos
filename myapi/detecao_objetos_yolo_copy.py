import os
import cv2
import numpy as np
from classificar_animais import classificar_animal  # Função para classificar animais com o modelo Random Forest

# Diretório onde este arquivo .py está localizado
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
YOLO_DIR = os.path.join(MODULE_DIR, 'C:/Users/dougl/myapi/myapi')  # Substitua pelo seu caminho real

def detectar_objetos(imagem_path):
    # Carrega os arquivos de configuração e pesos do YOLO
    net = cv2.dnn.readNet(os.path.join(YOLO_DIR, "yolov3.cfg"), os.path.join(YOLO_DIR, "yolov3.weights"))
    classes = []
    with open(os.path.join(YOLO_DIR, "coco.names"), "r") as f:
        classes = [line.strip() for line in f.readlines()]

    # Carrega a imagem usando o OpenCV
    imagem_opencv = cv2.imread(imagem_path)
    if imagem_opencv is None:
        print(f"Erro ao carregar a imagem: {imagem_path}")
        return

    # Detecta objetos na imagem
    blob = cv2.dnn.blobFromImage(imagem_opencv, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(get_output_layers(net))

    # Processa as detecções e retorna os resultados
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Objeto detectado com confiança
                center_x = int(detection[0] * imagem_opencv.shape[1])
                center_y = int(detection[1] * imagem_opencv.shape[0])
                w = int(detection[2] * imagem_opencv.shape[1])
                h = int(detection[3] * imagem_opencv.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Aplica supressão não-máxima para evitar detecções múltiplas do mesmo objeto
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Prepara os resultados
    resultados = {
        'objetos_detectados': [],
        'scores': [],
        'descricao_objetos': []
    }
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            resultados['objetos_detectados'].append(label)
            resultados['scores'].append(confidences[i])
            resultados['descricao_objetos'].append((x, y, w, h))

    # Classifica os animais detectados na imagem com o modelo Random Forest
    for i, objeto in enumerate(resultados['objetos_detectados']):
        if objeto == 'dog' or objeto == 'cat':
            # Região de interesse para classificação
            x, y, w, h = boxes[i]
            roi = imagem_opencv[y:y+h, x:x+w]
            # Classifica o animal na região de interesse
            classificacao = classificar_animal(roi)
            resultados['objetos_detectados'][i] = classificacao['objetos_detectados'][0]
            resultados['scores'][i] = classificacao['scores'][0]

    # Desenha os resultados na imagem
    for i in range(len(resultados['objetos_detectados'])):
        x, y, w, h = resultados['descricao_objetos'][i]
        label = resultados['objetos_detectados'][i]
        confidence = resultados['scores'][i]
        cv2.rectangle(imagem_opencv, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Ajustando a posição, o tamanho da fonte, a espessura e a cor do texto
        text = f'{label} {confidence:.2f}'
        # Coloca o texto à esquerda do retângulo, ajustando para evitar que saia da imagem
        text_x = x - 10 if x - 10 > 0 else x + w + 10
        text_y = y + 30 if y + 30 < imagem_opencv.shape[0] else y - 10
        cv2.putText(imagem_opencv, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, cv2.LINE_AA)

    # Mostra a imagem com as detecções
    cv2.imshow('Detecção de Objetos', imagem_opencv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return resultados

def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

# Caminho da imagem a ser processada
imagem_path = 'C:/Users/dougl/myapi/media/animais/cachorro/pastor-alemao/pastor.jpg'
detectar_objetos(imagem_path)
