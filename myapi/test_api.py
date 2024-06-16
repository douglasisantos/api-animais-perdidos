import requests

# URL da sua API
url = 'http://localhost:8000/enviar-animal-perdido/'

# Solicitar ao usuário os dados do animal perdido
nome = input("Digite o nome do animal: ")
tipo = input("Digite o tipo do animal: ")
raca = input("Digite o raca do animal: ")
endereco = input("Digite o endereco do animal: ")

# Caminho do arquivo de imagem
caminho_imagem = 'C:/Users/dougl/myapi/media/animais/cachorro/pastor-alemao/pastor.jpg'

# Dados do animal perdido
data = {
    'nome': nome,
    'tipo': tipo,
    'raca': raca,
    'endereco': endereco,
}

# Fazendo uma solicitação POST à sua API para enviar um animal perdido
with open(caminho_imagem, 'rb') as arquivo_imagem:
    response = requests.post(url, data=data, files={'foto': arquivo_imagem})

# Exibindo a resposta da API
print('Resposta da API:', response.text)
