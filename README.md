# Lista de Compras

Dois exercícios resolvidos de forma independente, cada um em sua própria pasta.

## Desafio 1 — `desafio_1_api/`

API REST para gerenciar uma lista de compras em memória (sem banco de dados), construída com FastAPI.

**Endpoints:**
- `POST /produtos` — adiciona um produto (corpo JSON: `{"nome": "Arroz"}`)
- `GET /produtos` — lista todos os produtos
- `GET /produtos/total` — retorna a quantidade de produtos
- `DELETE /produtos/{produto}` — remove um produto
- `PUT /produtos/{produto}/comprado` — marca um produto como comprado

**Como rodar:**
```bash
pip install -r requirements.txt
cd desafio_1_api
uvicorn api_rest:app --reload
```
Acesse `http://127.0.0.1:8000/docs` para testar os endpoints interativamente.

## Desafio 2 — `desafio_2/`

Classe `ListaCompras` com os métodos `adicionar`, `remover`, `listar`, `marcar_comprado` e `total`, gerenciando a lista em memória.

**Como rodar:**
```bash
cd desafio_2
python lista_compras.py
```
