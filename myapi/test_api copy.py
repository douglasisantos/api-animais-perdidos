import requests

# URL da sua API
url = 'http://localhost:8000/enviar-animal-perdido-api/'

# Dados do animal perdido (substitua pelos seus dados reais)
data = {
    'nome': 'Fida',
    'tipo': 'Cachorro',
    'raca': 'Cachorro',
    'endereco': 'Rua X, nº 123',
}

# Arquivo da foto
files = {'foto': open('C:/Users/dougl/myapi/media/animais/cachorro/pinscher/download (2).jpg', 'rb')}

# Faça a requisição POST para enviar o animal perdido
response = requests.post(url, data=data, files=files)

# Verifique se a requisição foi bem-sucedida
if response.status_code == 200:
    print('Animal perdido enviado com sucesso!')
    
    # Analisar a resposta JSON para obter os animais semelhantes, se houver
    response_json = response.json()
    if 'animais_perdidos_semelhantes' in response_json:
        animais_semelhantes = response_json['animais_perdidos_semelhantes']
        print('Animais semelhantes encontrados:')
        for animal in animais_semelhantes:
            print(f"Nome: {animal['nome']}, Tipo: {animal['tipo']}, Raça: {animal['raca']}")
else:
    print('Erro ao enviar animal perdido:', response.text)
