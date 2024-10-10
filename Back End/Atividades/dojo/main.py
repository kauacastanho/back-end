class Produto():
    def __init__(self, nome, custo, descricao) -> None:
        self.nome = nome
        self.custo = custo
        self.descricao = descricao
    
    def __str__(self):
        return f'{self.nome} , {self.custo}, {self.descricao}'
    

#class Prato(Produto):
   # def __init__(self, nome, custo, pdescricao, descricao) -> None:
       # self.nome = nome
       # self.custo = custo
        #self.descricao = descricao
        #self.pdescricao = pdescricao
       # Produto.__init__(nome, custo, descricao, pdescricao)

class Prato(Produto):
    def __init__(self, nome, listaprod, custo, descricao, preco):
        Produto.__init__(self, nome, custo, descricao)
        self.custo = custo
        self.descricao = descricao
        self.preco = preco
        self.nome = nome
        self.listaprod = listaprod
        
       

    def __str__(self):
        return f'{self.nome}, {self.listaprod} {self.custo}, {self.descricao}, {self.preco}'


class Bebida(Produto):
    def __init__(self, quantidade):
        self.quantidade = quantidade
        Produto.__init__(descricao)

class Vinho(Produto):
    def __init__(self, ano, descricao):
        self.ano = ano
        Produto.__init__(descricao)


produto1 = Produto("arroz", 7, "Arroz namorado") 
produto2 = Produto("feijao", 9, "feijao namorado") 

prato1 = Prato("arroz da  vovo", produto1, "arroz e feijao", "um arroz com feijao maravilhoso", 20)

print(prato1)