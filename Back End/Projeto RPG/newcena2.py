from metodos import esperar, resposta
from dicionario_de_respostas_v2 import dicionario_respostas
# ----------------------------------------------------------------------------------------------------------------------

# Código cena1 completa
# ----------------------------------------------------------------------------------------------------------------------


def cena2_0():
    print('\n[CENA 2 - CAMINHO ATÉ A CIDADE ALTA]\n')
    esperar()
    print('\nA euforia de um primeiro trabalho sempre acaba sendo memorável, e pra você não foi diferente.')
    esperar()
    print(
        '\nAs pessoas passam de cabeça baixa na rua, cada uma com suas questões e objetivos,'
        '\nmas chama a atenção aquele que está de cabeça erguida, o mais novo leão de mármore!')
    esperar()
    print('\nEm alguns minutos, a arquitetura muda de casas e lojas comuns e bem movimentadas para grandes palácios,'
          '\nmansões e pessoas chiques cruzando as ruas de Vevalon. Oficialmente na Cidade Alta.')
    esperar()
    print('\nTe foi dada duas opções, você pode procurar pelo contato da Katrina,'
          '\nou ir direto pro endereço indicado sem perder muito tempo.\n')
    resposta(dicionario_respostas["Cena2"]['parte1'],
            cena2_1,
            cena2_2)


def cena2_1():
    print('\nA esmo, você anda pelas ruas da cidade alta esperando encontrar alguém que chame sua atenção.')
    esperar()
    print('\nQuando sua atenção se perde por completo, uma mão te agarra pelo rosto e puxa beco adentro,'
          ' pondo a lâmina de uma adaga em seu pescoço.')
    esperar()
    print('\n???: Procurando alguém?')
    esperar()
    print('\nVocê se desespera por um segundo, mas lembra do que Katrina tinha falado. '
          '"Ela vai te achar antes de tu achar ela".\n')
    esperar()
    resposta(dicionario_respostas["Cena2"]['parte2'],
            cena2_3,
            cena2_4)


def cena2_2():
    print('\nA casa dos Anderson não é difícil de se encontrar.')
    esperar()
    print('\nAo andar em uma rua de chão cimentado, você vê alguns feiticeiros acendendo os postes e alguns membros'
          ' \nda alta classe perambulando e fofocando em frente a uma das grandes mansões do distrito.')
    esperar()
    print('\nVocê vê dentro dos portões desta casa, um cavalo com o leão da guilda queimado em sua pata.')
    esperar()


def cena2_3():
    print('\nQuem te mandou? A guarda real?\n')
    esperar()
    resposta(dicionario_respostas["Cena2"]['parte3'][0],
             cena2_5)


def cena2_4():
    print('\nKallista: Eu sou quem faz as perguntas, então fica de boa aí senão você vem pro chaveiro\n')
    esperar()
    resposta(dicionario_respostas["Cena2"]['parte3'][1],
             cena2_9)


def cena2_5():
    print('\nVocê sente a tensão da situação sumir completamente e a faca ficar mais leve no seu pescoço.')
    esperar()
    print('\nKallista: Ah, por que não disse antes? Vem cá colega!')
    esperar()
    print('\nA tiefling te puxa para um abraço caloroso. Ela é uma moça alta, pele lilás,'
          ' \nrabo longo e cabelo preso em uma grande trança.')
    esperar()
    print('\nVocê ouve alguns sussurros vindo dela e, apertando os olhos discretamente,'
          '\nnota em sua cintura um chaveiro com o que parecem almas saindo dele. É uma visão no mínimo arrepiante.')
    esperar()
    print('\nKallista: E aí, do que tá precisando?\n')
    esperar()
    resposta(dicionario_respostas["Cena2"]['parte4'],
             cena2_6,
             cena2_7,
             cena2_8)


def cena2_6():
    dicionario_respostas["Cena2"]['parte4'].remove("Qual a do chaveiro?")

    print('\nKallista: É um chaveiro de almas, elas me ajudam em algumas coisinhas, sabe?'
          ' Como se me falassem como fazer as coisas, né não pessoal?')
    esperar()
    print('\nVocê ouve sussurros lamentosos saindo do chaveiro, como uma prisão para aqueles que já se foram. '
          'Eles obviamente odeiam estar ali…')
    esperar()
    print('\nKallista: Eles me amam!\n')
    esperar()

    if len(dicionario_respostas["Cena2"]['parte4']) == 2:
        resposta(dicionario_respostas["Cena2"]['parte4'],
                 cena2_7,
                 cena2_8)
    elif len(dicionario_respostas["Cena2"]['parte4']) == 1:
        if dicionario_respostas["Cena2"]['parte4'][0] == "Quem é você mesmo?":
            resposta(dicionario_respostas["Cena2"]['parte4'],
                  cena2_7)
        elif dicionario_respostas["Cena2"]['parte4'][0] == ("A Katrina disse que você"
                                                            " sabe de algo do roubo, o que tem pra mim?"):
            resposta(dicionario_respostas["Cena2"]['parte4'],
                     cena2_8)
    elif len(dicionario_respostas["Cena2"]['parte4']) == 0:
        resposta(dicionario_respostas["Cena2"]['fim'],
                 cena2_2)


def cena2_7():
    dicionario_respostas["Cena2"]['parte4'].remove("Quem é você mesmo?")

    print('\nKallista: Eu sou Kallista! A ladina favorita da guilda e informante deles. '
          '\nQualquer coisa que você precisar, eu e meus colegas (vivos ou mortos) conseguimos para você! '
          '\nEm troca de algumas moedas, mas o que é um pequeno custo para uma informação tão valiosa, não é mesmo?\n')
    esperar()

    if len(dicionario_respostas["Cena2"]['parte4']) == 2:
        resposta(dicionario_respostas["Cena2"]['parte4'],
             cena2_6,
             cena2_8)
    elif len(dicionario_respostas["Cena2"]['parte4']) == 1:
        if dicionario_respostas["Cena2"]['parte4'][0] == "Quem é você mesmo?":
            resposta(dicionario_respostas["Cena2"]['parte4'],
                  cena2_7)
        elif dicionario_respostas["Cena2"]['parte4'][0] == ("A Katrina disse que você"
                                                            " sabe de algo do roubo, o que tem pra mim?"):
            resposta(dicionario_respostas["Cena2"]['parte4'],
                     cena2_8)
    elif len(dicionario_respostas["Cena2"]['parte4']) == 0:
        resposta(dicionario_respostas["Cena2"]['fim'],
                 cena2_2)

def cena2_8():
    dicionario_respostas["Cena2"]['parte4'].remove("A Katrina disse que você sabe de algo do roubo, o que tem pra mim?")

    print('\nKallista: Pelo que eu soube, foi um daqueles ovos Fabergé ou algo assim, saca?'
          ' O pai da família, o sir William, ta maluco com isso, dizendo que foi alguém de dentro.')
    esperar()
    print('\nKallista: O Marceu, nosso bardo e policial bonzinho, tá lá fazendo uma sondagem inicial. '
          'Fala com ele chegando lá e faz seu trabalho, sim? Boa sorte, novo-sangue!\n')
    esperar()

    if len(dicionario_respostas["Cena2"]['parte4']) == 2:
        resposta(dicionario_respostas["Cena2"]['parte4'],
                 cena2_6,
                 cena2_7)
    elif len(dicionario_respostas["Cena2"]['parte4']) == 1:
        if dicionario_respostas["Cena2"]['parte4'][0] == "Qual a do chaveiro?":
            resposta(dicionario_respostas["Cena2"]['parte4'],
                     cena2_6)
        elif dicionario_respostas["Cena2"]['parte4'][0] == "Quem é você mesmo?":
            resposta(dicionario_respostas["Cena2"]['parte4'],
                     cena2_7)
    elif len(dicionario_respostas["Cena2"]['parte4']) == 0:
        resposta(dicionario_respostas["Cena2"]['fim'],
                 cena2_2)


def cena2_9():
    print('\nKallista: Eu sou Kallista! A ladina favorita da guilda e informante deles.'
          '\nQualquer coisa que você precisar, eu e meus colegas (vivos ou mortos) conseguimos para você!')
    esperar()
    resposta(dicionario_respostas["Cena2"]['parte4'],
             cena2_6,
             cena2_7,
             cena2_8)


#cena2_0()
