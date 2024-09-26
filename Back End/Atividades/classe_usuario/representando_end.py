class Endereco:
    def __init__(self, logradouro, tipo_logradouro, numero, ponto_referencia, complemento, cep):
        self.logradouro = logradouro
        self.tipo_logradouro = tipo_logradouro
        self.numero = numero
        self.ponto_referencia = ponto_referencia
        self.complemento = complemento
        self.cep = cep



end1 = Endereco(
    logradouro = "Rua dr.eduardo silva",
    tipo_logradouro = "Rua",
    numero = "100",
    ponto_referencia = "Em frente a uma praça" ,
    complemento = "Casa",
    cep = "90245-040",
)

print(end1.logradouro)