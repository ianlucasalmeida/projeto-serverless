Conversor Serverless de Arquivos com FaaS
Visão Geral do Projeto
Este projeto implementa um sistema serverless para conversão e processamento de arquivos utilizando a abordagem Function as a Service (FaaS). A solução oferece uma interface web amigável para processamento de imagens e vídeos com armazenamento local, orquestração via Docker e estrutura modular inspirada em Ada.

Arquitetura do Sistema
Diagram
Code











Tecnologias Utilizadas
Componente	Tecnologia	Versão	Descrição
Linguagem Principal	Python	3.9	Linguagem base para toda a aplicação
Framework Web	Flask	2.1.0	Para criação da interface web
Processamento de Imagens	Pillow	9.1.0	Manipulação e conversão de imagens
Processamento de Vídeos	OpenCV	4.5.5	Para operações com vídeos e extração de frames
Containerização	Docker	-	Empacotamento da aplicação
Orquestração	Docker Compose	-	Gerenciamento de serviços
Armazenamento	Sistema de Arquivos	-	Armazenamento local com volumes Docker
Estrutura do Projeto
text
projeto-serverless/
├── main.py                 # Ponto de entrada: orquestra serviços e inicia a aplicação
├── Dockerfile              # Configuração do container principal
├── docker-compose.yml      # Definição dos serviços Docker
├── requirements.txt        # Dependências Python
├── app/                    # Módulo da aplicação
│   ├── web_app.py          # Aplicação Flask (frontend e rotas)
│   ├── image_processor.py  # Funções de processamento de imagem
│   ├── video_processor.py  # Funções de processamento de vídeo
│   ├── storage_manager.py  # Gerenciamento de armazenamento local
│   └── templates/          # Templates HTML
│       ├── index.html      # Página inicial para upload
│       └── result.html     # Página de resultado
├── uploads/                # Armazenamento de arquivos originais
└── processed/              # Armazenamento de arquivos processados
Funcionalidades Principais
Processamento de Imagens
Conversão para preto e branco

Redimensionamento (300x300 pixels)

Processamento de Vídeos
Conversão para formato MP4

Extração de frames:

Em minuto específico

Aleatória (quando nenhum minuto é especificado)

Interface Web
Upload de arquivos intuitivo

Seleção de operações específicas

Download de resultados processados

Como Executar o Projeto
Pré-requisitos
Docker e Docker Compose instalados

Git (para clonar o repositório)

Passo a Passo
Clonar o repositório:

bash
git clone https://github.com/seu-usuario/projeto-serverless.git
cd projeto-serverless
Construir e executar com Docker Compose:

bash
docker-compose up --build -d
Acessar a aplicação:
Abra o navegador em: http://localhost:5000

Utilizar a interface:

Selecione um arquivo (imagem ou vídeo)

Escolha a operação desejada

Para extração de frames de vídeo, especifique o minuto (ou deixe em branco para aleatório)

Clique em "Processar Arquivo"

Acessar resultados:

Após processamento, clique em "Download do Arquivo"

Arquivos processados estão em processed/

Arquivos originais estão em uploads/

Parar a aplicação:

bash
docker-compose down
Execução sem Docker (opcional)
bash
pip install -r requirements.txt
python main.py
Especificações Técnicas Detalhadas
main.py (Orquestrador Principal)
Inicia serviços Docker

Monitora saúde do sistema

Inicia aplicação Flask

Garante estabilidade com reinício automático

Módulo de Processamento de Imagens
Conversão para escala de cinza: Utiliza algoritmo de luminosidade

Redimensionamento: Mantém proporções com Pillow

Módulo de Processamento de Vídeos
Conversão para MP4: Usa codec H.264

Extração de frames: Baseada em FPS do vídeo

Frame aleatório: Seleção uniforme ao longo do vídeo

Armazenamento
Sistema de arquivos local

Persistência via volumes Docker

Estrutura organizada (uploads/originais, processed/resultados)

Interface Web
Design responsivo

Validação de tipos de arquivo

Feedback visual claro

Fluxo de Processamento
Diagram
Code
Possíveis Extensões
Integração com serviços cloud (AWS S3, Google Cloud Storage)

Suporte a mais formatos de arquivo

Processamento em lote de múltiplos arquivos

Sistema de filas para processamento assíncrono

Autenticação de usuários

Contribuição
Faça um fork do projeto

Crie uma branch para sua feature (git checkout -b feature/fooBar)

Commit suas mudanças (git commit -am 'Add some fooBar')

Push para a branch (git push origin feature/fooBar)

Abra um Pull Request

Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.

Contato
Para dúvidas ou sugestões: seu-email@exemplo.com