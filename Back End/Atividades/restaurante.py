class Produto:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f'{self.nome} {self.preco_format()}'

    def preco_format(self):
        return f'R$ {self.preco:0.2f}'


class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.__produtos = []

    def __str__(self):
        return f'{self.nome}'

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def tamanho_catalogo(self):
        return len(self.__produtos)

    def item_maior_valor(self):
        return max(self.__produtos, key=lambda p: p.preco)


restaurante = Restaurante('Mc Donalds')

produto1 = Produto('Mc Lanche Feliz', 'Com batata e refri', 34)
restaurante.adicionar_produto(produto1)
print(restaurante.tamanho_catalogo())

produto2 = Produto('Mc Flurry', 'Chocolate', 12)
restaurante.adicionar_produto(produto2)
print(restaurante.tamanho_catalogo())

produto3 = Produto('Big Mac', 'Apenas sanduiche', 11)
restaurante.adicionar_produto(produto3)
print(restaurante.tamanho_catalogo())

print(restaurante.item_maior_valor())

# Nao funciona, 'produtos' é privado
# print(restaurante.produtos)
