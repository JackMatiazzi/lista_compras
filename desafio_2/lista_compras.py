# Implemente uma classe ListaCompras que gerencie uma lista simples de produtos que precisam ser comprados.

# Sua classe deve ter os seguintes métodos:
# adicionar(produto) — Adiciona um novo produto ao final da lista. remover(produto) — Remove um produto específico da lista. 
# listar() — Retorna todos os produtos da lista. marcar_comprado(produto) — Marca um produto como comprado, adicionando "comprado" ao final do nome. 
# total() — Retorna o número total de produtos da lista.

# Exemplo de utilização:
# lista = ListaCompras() lista.adicionar("Arroz") lista.adicionar("Feijão") lista.adicionar("Leite") lista.marcar_comprado("Arroz") lista.remover("Leite") lista.listar()

# Resultado esperado:
# Arroz - comprado 
# Feijão


class ListaCompras:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def remover(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)

    def listar(self):
        return self.produtos

    def marcar_comprado(self, produto):
        try:
            indice = self.produtos.index(produto)
        except ValueError:
            return
        self.produtos[indice] = produto + " - comprado"

    def total(self):
        return len(self.produtos)


if __name__ == "__main__":
    lista = ListaCompras()
    lista.adicionar("Arroz")
    lista.adicionar("Feijão")
    lista.adicionar("Leite")
    lista.marcar_comprado("Arroz")
    lista.remover("Leite")
    for item in lista.listar():
        print(item)