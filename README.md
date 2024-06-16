# Meu Projeto YOLO

Este é um projeto que utiliza YOLOv3 para detecção de objetos em imagens de animais perdidos, e Random Forest para classificação dos animais detectados.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **detection_api/**: Contém os arquivos relacionados à API de detecção de animais perdidos.
  - **forms.py**: Formulários para captura de dados na API.
  - **models.py**: Definição dos modelos de dados, incluindo `AnimalPerdido`.
  - **serializers.py**: Serializadores para converter objetos Python em JSON.
  - **views.py**: Views que definem as APIs para enviar animais perdidos e processar as requisições.
- **media/**: Diretório onde as imagens de animais perdidos são armazenadas.
- **myapi/**: Configurações principais do projeto Django.
  - **settings.py**: Configurações do Django, incluindo definição de caminhos e ajustes de aplicativos.
  - **urls.py**: URLs do aplicativo, incluindo rotas para visualização e APIs.
  - **wsgi.py**: Ponto de entrada para o servidor WSGI.
- **modelos/**: Armazena o modelo treinado pelo Random Forest.
  - **modelo_random_forest.pkl**: Arquivo contendo o modelo treinado para classificação de animais.
- **detecao_objetos_yolo.py**: Script para detecção de objetos usando YOLOv3 em imagens.
- **carregar_imagens.py**: Script para carregar e preparar imagens para treinamento do modelo Random Forest.
- **test_api.py**: Script para testar a API de envio de animais perdidos.
- **README.md**: Este arquivo, contendo informações sobre como configurar e utilizar o projeto.

## Como Usar

Para utilizar o projeto, siga estas etapas:

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/meu-projeto-yolo.git
   cd meu-projeto-yolo
2. Instale as dependências necessárias. Certifique-se de estar usando um ambiente virtual Python:
    pip install -r requirements.txt
3. Para utilizar a API de envio de animais perdidos, execute o servidor Django:
    python manage.py runserver
4. Acesse a API em http://localhost:8000/enviar-animal-perdido-api/ para enviar dados de animais perdidos.

Se você deseja contribuir com este projeto, siga estas etapas:

Faça um fork deste repositório.

Crie uma branch com suas melhorias:
1. Crie uma branch com suas melhorias:  git checkout -b minha-feature
2. Faça commit das suas mudanças: git commit -am 'Adiciona minha nova feature
3.  Faça push para a branch: git push origin minha-feature

Autor Douglas Santos