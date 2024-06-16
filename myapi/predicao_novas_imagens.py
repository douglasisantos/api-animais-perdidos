import cv2
import numpy as np
import joblib

# Carregar o modelo treinado
rf_classifier = joblib.load('C:/Users/dougl/myapi/modelos/modelo_random_forest.pk1')  

# Carregar a nova imagem
nova_imagem_path = "C:/Users/dougl/myapi/treinamento/kkk.jpg"
nova_imagem = cv2.imread(nova_imagem_path)

# Pré-processar a imagem, se necessário
nova_imagem_redimensionada = cv2.resize(nova_imagem, (500, 500))  # Redimensionar para o mesmo tamanho usado durante o treinamento

# Transformar a imagem em um vetor unidimensional, se necessário
nova_imagem_vetor = nova_imagem_redimensionada.flatten()

# Fazer a predição usando o modelo treinado
classe_predita = rf_classifier.predict([nova_imagem_vetor])

# Interpretar o resultado da predição
print("A classe predita para a nova imagem é:", classe_predita)
