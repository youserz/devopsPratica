# FastAPI Hello World

Aplicação simples desenvolvida com Python e FastAPI para o exercício prático de Docker, GitHub Actions e Container Registry.

## Executando localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```
Execute a aplicação:
```bash
uvicorn app.main:app --reload
```
Acesse:

http://localhost:8000/hello
Executando com Docker

Criar a imagem:
```bash
docker build -t fastapi-hello:1.0 .
```
Executar o container:
```bash
docker run -p 8000:8000 fastapi-hello:1.0
```
Acesse:

http://localhost:8000/hello

Resposta esperada:
```bash
"Hello World"
```