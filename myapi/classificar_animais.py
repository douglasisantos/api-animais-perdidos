import os
import cv2
import numpy as np
import joblib  # Importa a função joblib para carregar o modelo Random Forest

# Diretório onde este arquivo .py está localizado
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELOS_DIR = os.path.join(MODULE_DIR, 'C:/Users/dougl/myapi/modelos')  # Substitua pelo seu caminho real

def classificar_animal(imagem):
    # Carregar o modelo Random Forest treinado
    modelo_random_forest = joblib.load(os.path.join(MODELOS_DIR, 'modelo_random_forest.pk1'))

    # Pré-processar a imagem, se necessário
    imagem_redimensionada = cv2.resize(imagem, (500, 500))  # Redimensionar para o mesmo tamanho usado durante o treinamento
    imagem_vetor = imagem_redimensionada.flatten()  # Transformar a imagem em um vetor unidimensional

    # Fazer a predição usando o modelo treinado
    classe_predita = modelo_random_forest.predict([imagem_vetor])

    return {
        'objetos_detectados': classe_predita.tolist(),
        'scores': [1.0]  # Supomos que a confiança seja 100% para a classe prevista
    }

