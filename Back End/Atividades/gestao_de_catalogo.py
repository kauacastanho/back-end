class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def __str__(self):
        return f"{self.nome} - {self.preco}"


    def __eq__(self, outro_produto):
            return (
                self.nome.lower() == outro_produto.nome.lower() and 
                self.preco == outro_produto.preco
            )


class Restaurante:

    LIMIT_PRODUCTS = 10

    def __init__(self, nome):
        self.nome = nome
        self.products = []

    def __str__(self):
        return f"{self.nome}"

    def can_add_item(self):
        return len(self.products) < Restaurante.LIMIT_PRODUCTS

    def adicionar_produto(self, novo_produto):
        if not isinstance(novo_produto, Produto):
            raise NotAProductError()
        if not self.can_add_item():
            raise FullCatalogError(Restaurante.LIMIT_PRODUCTS)
        if novo_produto not in self.products:
            self.products.append(novo_produto)  

    def remover_produto(self, novo_produto):
        if not isinstance(novo_produto, Produto):
            raise NotAProductError()
        if novo_produto in self.products:
            self.products.remove(novo_produto)
        else:    
            raise ProductNotFoundError()


class ProductNotFoundError(Exception):
    def __init__(self):
        super().__init__("Produto não encontrado no catálogo")

class NotAProductError(Exception):
    def __init__(self):
        super().__init__("Objeto informado não é um produto")

class FullCatalogError(Exception):
    def __init__(self, limit):
        super().__init__(f"Catálogo já possui {limit} itens")


pizza1 = Produto("Pizza 1 queijos", 31)
pizza1b = Produto("Pizza 1 queijos", 31)
pizza2 = Produto("Pizza 2 queijos", 32)
pizza3 = Produto("Pizza 3 queijos", 33)
pizza4 = Produto("Pizza 4 queijos", 34)
pizza5 = Produto("Pizza 5 queijos", 35)
pizza6 = Produto("Pizza 6 queijos", 36)
pizza7 = Produto("Pizza 7 queijos", 37)
pizza8 = Produto("Pizza 8 queijos", 38)
pizza9 = Produto("Pizza 9 queijos", 39)
pizza10 = Produto("Pizza 10 queijos", 40)
#pizza11 = Produto("Pizza 11 queijos", 41)

sushi = Produto("Sushi", 50)

restaurante = Restaurante("Pizzaria X")
restaurante.adicionar_produto(pizza1)
restaurante.adicionar_produto(pizza2)
restaurante.adicionar_produto(pizza3)
restaurante.adicionar_produto(pizza4)
restaurante.adicionar_produto(pizza5)
restaurante.adicionar_produto(pizza6)
restaurante.adicionar_produto(pizza7)
restaurante.adicionar_produto(pizza8)
restaurante.adicionar_produto(pizza9)
restaurante.adicionar_produto(pizza10)
#restaurante.adicionar_produto(pizza11)
#restaurante.remover_produto(sushi)

if pizza1 == pizza1b:
    print("pizza1 == pizza1b")

######### CODIGO FUNCIONANDO