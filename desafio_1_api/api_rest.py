# Desenvolva uma API REST para gerenciar uma lista de compras. A API deverá permitir que um cliente possa adicionar, remover, consultar e marcar produtos como comprados.

# A aplicação deverá manter uma lista de produtos em memória, não sendo necessário utilizar banco de dados.

# Endpoints necessários:
# - POST /produtos deve receber o nome do produto e adicioná-lo à lista.
# - GET /produtos deve retornar todos os produtos cadastrados.
# - DELETE /produtos/{produto} deve remover o produto informado.
# - PUT /produtos/{produto}/comprado deve alterar o estado do produto para comprado.
# - GET /produtos/total deve retornar a quantidade de produtos cadastrados.
# As respostas da API deverão utilizar o formato JSON.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

produtos = []


class ProdutoInput(BaseModel):
    nome: str


@app.post("/produtos", status_code=201)
def adicionar_produto(produto: ProdutoInput):
    for item in produtos:
        if item["nome"] == produto.nome:
            raise HTTPException(status_code=409, detail="produto ja existe")
    produtos.append({"nome": produto.nome, "comprado": False})
    return {"nome": produto.nome, "comprado": False}


@app.get("/produtos")
def listar_produtos():
    return {"produtos": produtos}


@app.get("/produtos/total")
def total_produtos():
    return {"total": len(produtos)}


@app.delete("/produtos/{produto}")
def remover_produto(produto: str):
    for indice, item in enumerate(produtos):
        if item["nome"] == produto:
            produtos.pop(indice)
            return {"mensagem": "produto removido "}
    raise HTTPException(status_code=404, detail="produto não encontrado")

@app.put("/produtos/{produto}/comprado")
def marcar_comprado(produto: str):
    item = next((item for item in produtos if item["nome"] == produto), None)
    if item:
        item["comprado"] = True
        return {"mensagem": "produto comprado"}
    else:
        raise HTTPException(status_code=404, detail="produto não encontrado")
