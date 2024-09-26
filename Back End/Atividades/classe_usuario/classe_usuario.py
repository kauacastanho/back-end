from representando_end import Endereco

class usuario:
    def __init__(self, nome, sobrenome, email, endereco):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__endereco = endereco

    def __str__(self):
        return f'{self.__nome}'{self.__logradouro}

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self.dado):
        return self.__nome = dado

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self.dado):
        return self.__sobrenome = dado

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self.dado):
        return self.__email = dado

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self.dado)
        return self.__email

u = usuario(
    nome = "kauã",
    sobrenome = "castanho",
    email = "kaua@atitus.com",
    endereco = "sete"
)

endereco2 = Endereco(
    logradouro = "Rua dr.eduardo silva",
    tipo_logradouro = "Rua",
    numero = "100",
    ponto_referencia = "Em frente a uma praça" ,
    complemento = "Casa",
    cep = "90245-040",
)

print(u)
