import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Função para extrair características das imagens
def extrair_caracteristicas(imagem):
    # Redimensionar a imagem para um tamanho fixo (opcional)
    # image = cv2.resize(image, (largura, altura))

    # Extrair características (média das intensidades de cor em cada canal RGB)
    mean_rgb = np.mean(imagem, axis=(0, 1))
    return mean_rgb

# Caminhos para as imagens de treinamento
pastor_alemao_path = "C:/Users/dougl/Desktop/TESTETCC/treinamento/pastor.jpg"
shihtzu_path = "C:/Users/dougl/Desktop/TESTETCC/treinamento/shih-tzu.jpg"
pinscher_path = "C:/Users/dougl/Desktop/TESTETCC/treinamento/pinscher.jpg"

# Carregar as imagens de treinamento
pastor_alemao = cv2.imread(pastor_alemao_path)
shihtzu = cv2.imread(shihtzu_path)
pinscher = cv2.imread(pinscher_path)

# Extrair características das imagens
X_train = []
y_train = []

for imagem in [pastor_alemao, shihtzu, pinscher]:
    features = extrair_caracteristicas(imagem)
    X_train.append(features)

# Codificar as classes (raças de cachorro)
y_train = [0, 1, 2]  # Pastor Alemão = 0, Shih Tzu = 1, Pinscher = 2

# Inicializar e treinar o classificador KNN
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train, y_train)

# Agora o classificador KNN está treinado e pronto para fazer previsões
