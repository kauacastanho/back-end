from abc import ABC, abstractmethod


class Produto(ABC):
    
    @abstractmethod
    def custo_toal(self):
        '''Mostra o custo total'''
        pass

    def mostrar_detalhes(self):
        pass

class Pizza(Produto):

    def __init__(self, custo_massa, custo_queijo):
        self.custo_massa = custo_massa
        self.custo_queijo = custo_queijo

    def custo_total(self):
        return self.custo_massa + self.custo_queijo

class Sushi(Produto):

    def __init__(self, custo_peixe, custo_arroz):
        self.custo_peixe = custo_peixe
        self.custo_arroz = custo_arroz

    def custo_total(Self):
        return self.custo_peixe + self.custo_arroz


def calcula_totais(lista_pizza, lista_sushi):
    soma = 0

    for pizza in lista_pizza:
        soma += pizza.custo_total()
    for sushi in lista_sushi:
        soma += sushi.custo_total()
    
    return soma


pizza = Pizza(custo_massa=10, custo_queijo=3)
pizza2 = Pizza(custo_massa=8, custo_queijo=6)

sushi = Sushi(custo_arroz=7, custo_peixe=10)
sushi2 = Sushi(custo_arroz=3, custo_peixe=8)

print(calcula_totais(pizza))
print(calcula_totais(pizza2))
print(calcula_totais(sushi))
print(calcula_totais(sushi2))

