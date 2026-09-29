Exercício Prático — Docker, GitHub Actions e Container Registry

Aplicação simples desenvolvida em Python utilizando FastAPI, com containerização utilizando Docker, integração contínua com GitHub Actions e publicação automática das imagens no GitHub Container Registry (GHCR).

1. Tecnologias utilizadas

Python 3.12

FastAPI

Uvicorn

Docker

GitHub

GitHub Actions

GitHub Container Registry (GHCR)

2. Aplicação

A aplicação possui o endpoint HTTP:

GET /hello

Versão 1.0

A primeira versão da aplicação retorna:

Hello World

Versão 2.0

Após a alteração solicitada no exercício, a aplicação passou a retornar:

Hello World 2

3. Execução local da aplicação

Para executar a aplicação diretamente com Python, instale as dependências:

pip install -r requirements.txt


Depois, execute a aplicação:

uvicorn app.main:app --reload


A aplicação ficará disponível em:

http://localhost:8000


O endpoint pode ser testado com:

curl http://localhost:8000/hello

4. Docker

A aplicação possui um Dockerfile na raiz do projeto.

Para criar uma imagem local:

docker build -t fastapi-hello:1.0 .


Para executar o container:

docker run --rm -p 8000:8000 fastapi-hello:1.0


O endpoint pode ser testado com:

curl http://localhost:8000/hello


Na primeira versão, o resultado esperado é:

"Hello World"

5. GitHub Actions

A pipeline está localizada em:

.github/workflows/docker.yml


A execução da pipeline ocorre automaticamente após um push para a branch main.

O fluxo da pipeline é:

Código
  ↓
Checkout
  ↓
Build da imagem Docker
  ↓
Verificação da imagem
  ↓
Login no GitHub Container Registry
  ↓
Push da imagem


A autenticação com o GitHub Container Registry utiliza o mecanismo de autenticação fornecido pelo GitHub Actions, sem armazenar credenciais diretamente no código da pipeline.

6. Container Registry

As imagens são publicadas no GitHub Container Registry (GHCR).

Versão 1.0
ghcr.io/youserz/devopspratica:1.0

Versão 2.0
ghcr.io/youserz/devopspratica:2.0

7. Versão 1.0

A primeira versão foi construída e publicada pela pipeline com a tag:

ghcr.io/youserz/devopspratica:1.0

Baixar a imagem
docker pull ghcr.io/youserz/devopspratica:1.0

Executar o container
docker run --rm -p 8000:8000 ghcr.io/youserz/devopspratica:1.0

Testar o endpoint
curl http://localhost:8000/hello


Resultado esperado:

"Hello World"

8. Versão 2.0

A aplicação foi alterada para retornar:

Hello World 2


Após um novo commit e push para a branch main, a pipeline foi executada novamente e publicou a nova imagem:

ghcr.io/youserz/devopspratica:2.0

Baixar a imagem
docker pull ghcr.io/youserz/devopspratica:2.0

Executar o container
docker run --rm -p 8000:8000 ghcr.io/youserz/devopspratica:2.0

Testar o endpoint
curl http://localhost:8000/hello


Resultado esperado:

"Hello World 2"

9. Fluxo completo

O fluxo implementado no projeto é:

Desenvolvedor
     ↓
  git push
     ↓
Repositório GitHub
     ↓
GitHub Actions
     ↓
Build da imagem Docker
     ↓
Publicação no GHCR
     ↓
  docker pull
     ↓
Execução local
     ↓
Teste do endpoint


O fluxo foi realizado para as versões 1.0 e 2.0.

10. Repositório
GitHub

https://github.com/youserz/devopsPratica

Container Registry
ghcr.io/youserz/devopspratica