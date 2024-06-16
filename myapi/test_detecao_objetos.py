import unittest
import cv2
import os
from detecao_objetos_yolo import detectar_objetos  # Importe a função detectar_objetos

class TestDetecaoObjetos(unittest.TestCase):
    def test_detectar_objetos(self):
        # Caminho completo para o arquivo de imagem de exemplo
        foto_exemplo = "C:/Users/dougl/myapi/treinamento/kkk.jpg"

        # Verificar se o arquivo de imagem existe
        if not os.path.isfile(foto_exemplo):
            raise FileNotFoundError(f"O arquivo {foto_exemplo} não foi encontrado.")

        # Abrir a imagem em modo de leitura binária
        with open(foto_exemplo, 'rb') as imagem:
            resultados = detectar_objetos(imagem)

        # Verificar se os resultados não são nulos
        self.assertIsNotNone(resultados)
        # Adicione mais asserções conforme necessário para validar os resultados
if __name__ == '__main__':
    unittest.main()