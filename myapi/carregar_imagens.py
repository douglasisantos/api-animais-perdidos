import os  # Importa a biblioteca os, usada para interagir com o sistema operacional, como manipulação de arquivos e diretórios.
import cv2  # Importa a biblioteca OpenCV, usada para processamento de imagens e visão computacional.
import numpy as np  # Importa a biblioteca numpy e a apelida de 'np', usada para operações matemáticas e manipulação de arrays.
from sklearn.model_selection import train_test_split  # Importa a função train_test_split do scikit-learn, usada para dividir os dados em conjuntos de treinamento e teste.
from sklearn.ensemble import RandomForestClassifier  # Importa a classe RandomForestClassifier do scikit-learn, usada para criar e treinar um modelo de floresta aleatória.
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score  # Importa funções do scikit-learn para calcular métricas de avaliação de modelos.
import seaborn as sns  # Importa a biblioteca seaborn, usada para criação de gráficos estatísticos, especialmente para visualização de dados.
import matplotlib.pyplot as plt  # Importa o módulo pyplot da biblioteca matplotlib e o apelida de 'plt', usado para criação de gráficos e visualizações.
import joblib  # Importa a biblioteca joblib, usada para salvar e carregar modelos treinados.

# Diretório onde as imagens estão localizadas
IMAGES_DIR = "C:/Users/dougl/myapi/media/animais"
NEW_SIZE = (500, 500)  # Defina o tamanho desejado para as imagens redimensionadas

def carregar_imagens():
    imagens = []
    labels = []

    # Percorre recursivamente os subdiretórios
    for root, dirs, files in os.walk(IMAGES_DIR):
        for filename in files:
            # Verifica se o arquivo é uma imagem
            if filename.endswith(".jpg") or filename.endswith(".png"):
                # Carrega a imagem
                image_path = os.path.join(root, filename)
                image = cv2.imread(image_path)
                if image is not None:
                    # Redimensiona a imagem para o tamanho desejado
                    resized_image = cv2.resize(image, NEW_SIZE)
                    # Adiciona a imagem e a classe ao conjunto de dados
                    imagens.append(resized_image.flatten())  # Transforma a imagem em um vetor unidimensional
                    label = os.path.basename(os.path.dirname(image_path))
                    labels.append(label)

    return imagens, labels

# Carregar imagens e labels
imagens, labels = carregar_imagens()

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(imagens, labels, test_size=0.2, random_state=42)

# Exibir o número de imagens em cada conjunto
print("Número de imagens no conjunto de treinamento:", len(X_train))
print("Número de imagens no conjunto de teste:", len(X_test))

# Criar e treinar o modelo RandomForest
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)

# Salvar o modelo treinado
MODELOS_DIR = "C:/Users/dougl/myapi/modelos"
if not os.path.exists(MODELOS_DIR):
    os.makedirs(MODELOS_DIR)
joblib.dump(rf_classifier, os.path.join(MODELOS_DIR, "modelo_random_forest.pkl"))

# Prever as classes no conjunto de teste
y_pred = rf_classifier.predict(X_test)

# Calcular a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)

# Exibir a matriz de confusão como um heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=rf_classifier.classes_, yticklabels=rf_classifier.classes_)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# Calcular a precisão para cada classe
precisao_por_classe = precision_score(y_test, y_pred, average=None)

# Calcular a revocação para cada classe
revocacao_por_classe = recall_score(y_test, y_pred, average=None)

# Calcular o F1-Score para cada classe
f1_por_classe = f1_score(y_test, y_pred, average=None)

# Exibir as métricas para cada classe
for classe, precisao, revocacao, f1 in zip(rf_classifier.classes_, precisao_por_classe, revocacao_por_classe, f1_por_classe):
    print(f"Classe: {classe}")
    print(f"Precisão: {precisao}")
    print(f"Revocação: {revocacao}")
    print(f"F1-Score: {f1}\n")