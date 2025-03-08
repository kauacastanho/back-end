import os

frase_criptografada = "ÔZÜZ.QÓÇK#CÕ,RI#!Ó,ÕÓAÜÕB#Z#,ÃZC!#ÔZÜZ#;!,ÜÀ?ÜZÜ#Z#?ÜZÇ!#Ç!,Ü!AZ#,ÕÓAÀÓB!#Ç!BÇ#!ÇAB;ÕÇ#!#A!ÓÃZ#ÍBÀAÕ#ÇB,!ÇÇÕKK#"

alfabeto = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    ".", ",", ";", "!", "?", "Á", "Ã", "À", "Â", "É", "Í", "Ó", "Õ", 
    "Ô", "Ú", "ü", "Ç"
]


def carregar_dicionario():
    nome_arquivo = "dicionario.txt"
    pasta_atual = os.path.dirname(os.path.abspath(__file__))  
    caminho_arquivo = os.path.join(pasta_atual, nome_arquivo)  
    dicionario = set()

    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dicionario.add(linha.strip().lower())  # Adiciona palavras normalizadas
    else:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
    
    return dicionario

def verificar_no_dicionario(palavra, dicionario):
    if palavra.lower() in dicionario:
        return True
    return False

def proximo_caractere(caractere):
    """Retorna o próximo caractere no alfabeto"""
    if caractere in alfabeto:
        indice = alfabeto.index(caractere)
        prox_carac = alfabeto[(indice + 1) % len(alfabeto)] 
        return prox_carac  # Se passar do último, volta ao primeiro
    return caractere  # Retorna o mesmo caractere se não estiver no alfabeto

def separa_frases(frase_criptografada):
    frase_separada = frase_criptografada.split('#')
    return frase_separada

def caractere_atual(frase_separada):
    caracteres_separados = [] # Criando uma lista para armazenar os caracteres da frase
    for caractere in frase_separada[0]:
        caracteres_separados.append(caractere) # Adicionando cada caractere da frase na lista 
    return caracteres_separados[0] # Retornando o primeiro caractere da palavra


dict = carregar_dicionario()

separar = separa_frases(frase_criptografada)

caractere_a = caractere_atual(separar)

prox = proximo_caractere(caractere_a)