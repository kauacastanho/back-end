from metodos import esperar, resposta
from dicionario_de_respostas_v2 import dicionario_respostas
from introducao import introducao

# ----------------------------------------------------------------------------------------------------------------------

# Código cena1 completa
# ----------------------------------------------------------------------------------------------------------------------

global n
n = 0


def funcao_dialogos_extra(lista_opcoes_e_respostas: list, continuacao_historia=None):

    resposta(lista_opcoes_e_respostas[0], lista_opcoes_e_respostas[1])
    esperar()
    print('\nKatrina: Você já fez perguntas demais. Vamos começar o trabalho logo.')
    esperar()

    if continuacao_historia is None:
        print('Erro')
        exit()

    else:
        continuacao_historia()


def cena1():
    print('\nAperte ENTER para prosseguir.\n')
    esperar()
    print("\n\n\n"
          " _                                _        __  __\n"
          "| |                              | |      |  \\/  |\n"
          "| |     ___  ___   ___  ___    __| | ___  | \\  / | __ _ _ __ _ __ ___   ___  _ __ ___\n"
          "| |    / _ \\/ _ \\ / _ \\/ __|  / _` |/ _ \\ | |\\/| |/ _` | '__| '_ ` _ \\ / _ \\| '__/ _ \\ \n"
          "| |___|  __/ (_) |  __/\\__ \\ | (_| |  __/ | |  | | (_| | |  | | | | | | (_) | | |  __/\n"
          "|______\\___|\\___/ \\___||___/  \\__,_|\\___| |_|  |_|\\__,_|_|  |_| |_| |_|\\___/|_|  \\___|\n\n\n")
    esperar()
    introducao()
    esperar()
    print('\nPassaram alguns dias desde que esse pequeno cartaz chamou sua atenção em um dos becos próximos do porto '
          'do reino. Você revirou algumas gavetas\nprocurando uma curta espada e plaquetas de armadura herdadas de '
          'família ou amigos e, com entusiasmo, entrou pelas portas da pequena sede da guilda.')
    esperar()
    print('\nAlgumas pessoas estão espalhadas pelas mesas no pequeno salão, algumas escolhendo comissões em um '
          'grande quadro… mas uma se destaca. Uma meia-elfa com\nidade já mais avançada, loira, cicatriz no rosto '
          'e arco nas costas acena para você com um sorriso no rosto.')
    esperar()
    print('\n???: Bom dia!! Veio se juntar a guilda, sangue-novo?')
    esperar()

    resposta(dicionario_respostas['Cena1']['parte1'], cena1_parte1_caminho1,
             cena1_parte1_caminho2)

    resposta(dicionario_respostas['Cena1']['parte2'][0], cena1_parte2_caminho1,
             cena1_parte2_caminho2, cena1_parte2_caminho3)


# ----------------------------------------------------------------------------------------------------------------------

# Código divido

# Primeira parte de cena 1(Linhas 33-60 da cena 1)
# ----------------------------------------------------------------------------------------------------------------------


# Reposta para 'Nah, só to a passeio…' (Linha 33)
def cena1_parte1_caminho1():
    print('\n???: Bem… fica à vontade, mas não se enrola muito, tem gente querendo trabalhar aqui.')
    esperar()
    print('\nNo fim das contas, toda sua dedicação e entusiasmo foram completamente passageiros, e quando ficou de '
          'frente com o seu destino, decidiu dar um passo \natrás para viver uma vida pacata.\n\nGame Over.')
    exit()


# Reposta para 'Claro! Por onde eu começo?'  e 'Bora' (Linha 41), (resposta não presente no roteiro)
def cena1_parte1_caminho2():
    print('\nMayla: Ótimo! Eu sou Mayla, a líder da guilda e com quem você vai pegar novas comissões, ok? Como é o seu'
          ' começo, eu tenho aqui um caso de roubo perto\nda Cidade Alta. Conversa com a Senhorita Kat, '
          'ela tá… descansando.')
    esperar()
    print('\nVocê se vira para procurar a tal garota que Mayla e, de fato, lá está, uma jovem garota deitada em cima de'
          ' umas mesas com um caneco na mão e...\num urso de metal ao lado dela?')
    esperar()
    print('\nApertando bem os olhos, percebe que realmente não se enganou, ela se levanta da mesa aos tropeços e se '
          'encosta no grande robô. Ele solta vapor\nde suas juntas e solta um bufado rouco.')
    esperar()
    print('\nEla usa um vestido puído, cabelos ruivos, sardas e duas machadinhas em sua cintura. Do seu conhecimento, '
          'ela parece uma pirata que você ouviu falar\na alguns anos atrás, Katrina Strand, uma artífice que andava '
          'com um tal de Bruno. Você acabou de descobrir quem é esse ser desconhecido...')
    esperar()
    print('\nKatrina: Opa e aí? Eu sou a Katrina, mas pode me chamar de Kat! A Mayla te mandou, não foi?\n')


# ----------------------------------------------------------------------------------------------------------------------

# Segunda parte da cena 1(Linhas 62- 95)
# ----------------------------------------------------------------------------------------------------------------------


# Reposta para 'Não, acho que me arrependi de estar aqui' (Linha 62)
def cena1_parte2_caminho1():
    print('\nKatrina: Vai lá, frangote.')
    esperar()
    print('\nApesar do insulto, é impossível recusar ele. Você fugiu com o rabo entre as pernas na primeira '
          'anormalidade que apareceu. Uma vida triste e parada \nte espera!\n\nGame Over.')
    exit()


# Reposta para 'Sim! Mas antes…' (Linha 68)
def cena1_parte2_caminho2():

    perguntas_feitas = 0
    continuar_perguntando = ''
    lista = [[dicionario_respostas['Cena1']['parte2'][1][0], dicionario_respostas['Cena1']['parte2'][1][1],
             dicionario_respostas['Cena1']['parte2'][1][2]], dialogo_extra1, dialogo_extra2, dialogo_extra3]
    print('\nKatrina: O  que foi?\n')

    while continuar_perguntando != '1':

        if continuar_perguntando != '2':
            caminho = resposta(lista[0], lista[1], lista[2], lista[3])

        else:

            match caminho:

                case 0:

                    if perguntas_feitas == 0:
                        perguntas_feitas = resposta([lista[0][1], lista[0][2]], lista[2], lista[3])

                    elif perguntas_feitas == 1:
                        funcao_dialogos_extra([[lista[0][2]], lista[3]], cena1_parte2_caminho3)
                        break

                    elif perguntas_feitas == 2:
                        funcao_dialogos_extra([[lista[0][1]], lista[2]], cena1_parte2_caminho3)
                        break

                case 1:

                    if perguntas_feitas == 0:

                        perguntas_feitas = resposta([lista[0][0], lista[0][2]], lista[1], lista[3])

                        if perguntas_feitas == 0:
                            perguntas_feitas += 1

                    elif perguntas_feitas == 1:

                        funcao_dialogos_extra([[lista[0][2]], lista[3]], cena1_parte2_caminho3)
                        break

                    elif perguntas_feitas == 2:

                        funcao_dialogos_extra([[lista[0][0]], lista[1]], cena1_parte2_caminho3)
                        break

                case 2:

                    if perguntas_feitas == 0:
                        perguntas_feitas = resposta([lista[0][0], lista[0][1]], lista[1], lista[2])
                        if perguntas_feitas == 0:
                            perguntas_feitas += 2

                    elif perguntas_feitas == 1:
                        funcao_dialogos_extra([[lista[0][0]], lista[1]], cena1_parte2_caminho3)
                        break

                    elif perguntas_feitas == 2:
                        funcao_dialogos_extra([[lista[0][1]], lista[2]], cena1_parte2_caminho3)
                        break

        esperar()
        print('\nKatrina: Mas e aí? Pronto pra missão?\n')

        continuar_perguntando = input('1: Claro, vamos nessa!\n2: Ainda não, tenho mais uma pergunta...\n')

        while continuar_perguntando != '1' and continuar_perguntando != '2':
            print('Por favor, digite um dos números indicados.')
            continuar_perguntando = input('1: Claro, vamos nessa!\n2: Ainda não, tenho mais uma pergunta...\n')

        if continuar_perguntando == '2':
            print('\nKatrina: Qual?\n')

        else:
            cena1_parte2_caminho3()
            break


# Reposta para 'Sim, me diz ai o que tu sabe.' ou 'Claro, vamos nessa!' (Linha 89), (linha 87)
def cena1_parte2_caminho3():
    print('\nKatrina: Bom, eu conheço uma ladina que fica que ta sempre rondando por aí com aquele chaveiro esquisito '
          'dela. Ela me falou sobre esse\nroubo à casa Anderson. Eles moram na cidade alta, '
          'então pode esperar por gente chata. Ela também disse que esse roubo não tem relação\ncom a facção de '
          'ladinos da cidade, nem é território '
          'deles lá. Tu pode procurar por ela ou ir direto pra casa Anderson tentar entender.')
    esperar()
    print('\nKatrina: Alguma dúvida?')
    esperar()
    resposta(dicionario_respostas['Cena1']['parte3'], cena1_parte3_caminho1, cena1_parte3_caminho2, cena1_parte3_caminho3)


# ----------------------------------------------------------------------------------------------------------------------

# Terceira parte da cena 1(Linhas 97-107)
# ----------------------------------------------------------------------------------------------------------------------


# Reposta para 'Qual o nome dessa ladina?' (Linha 97)
def cena1_parte3_caminho1():
    global n
    n += 1

    print('\nKatrina: Kallista, mas nem se preocupe, ela vai te achar antes de tu achar ela. Ela sempre me '
          'assusta assim…')
    esperar()
    print('\nKatrina: Alguma dúvida?')
    esperar()

    if n == 1:
        resposta([dicionario_respostas['Cena1']['parte3'][1], dicionario_respostas['Cena1']['parte3'][2]], cena1_parte3_caminho2, cena1_parte3_caminho3)

    else:
        resposta([dicionario_respostas['Cena1']['parte3'][2]], cena1_parte3_caminho3)

# Reposta para 'O que foi roubado exatamente?' (Linha 101)


def cena1_parte3_caminho2():
    global n

    n -= 2
    print('\nKatrina: Uma jóia, aparentemente. Algo de várias gerações da família e tal. Provavelmente foi algo '
          'envolvendo aquelas briguinhas\npolíticas idiotas de gente idiota.')
    esperar()
    print('\nKatrina: Alguma dúvida?')
    esperar()

    if n == -2:
        resposta([dicionario_respostas['Cena1']['parte3'][0], dicionario_respostas['Cena1']['parte3'][2]], cena1_parte3_caminho1, cena1_parte3_caminho3)

    else:
        resposta([dicionario_respostas['Cena1']['parte3'][2]], cena1_parte3_caminho3)


# Reposta para 'Já, tô de saída.' (Linha 106)
def cena1_parte3_caminho3():
    print('\nKatrina: Boa sorte, marujo!')
    esperar()


# ----------------------------------------------------------------------------------------------------------------------

# Repostas para as perguntas das linhas  69-84 da cena 1
# ----------------------------------------------------------------------------------------------------------------------

# Reposta para 'Quem é você?' (Linha 69)
def dialogo_extra1():
    print('\nKatrina: Katrina! Eu era pirata quando menor, fazia uns bicos e uns roubos… Você já deve ter ouvido meu'
          ' nome por aí. Decidi dar uma parada e\nacabei por aqui mesmo.'
          ' O resto você vai descobrindo com o tempo, sim?')

    return 0


# Reposta para 'Qual é a do urso?' (Linha 75)


def dialogo_extra2():
    print('\nKatrina: Esse aí é o Bruno! Ele ainda precisa de uns toques, mas é um ótimo escudo móvel e guerreiro'
          ' implacável! Não é Bruno?')
    esperar()
    print('\nBruno: Bruno!')
    esperar()
    print('\nKatrina: Eu ainda tô ensinando ele a falar.')

    return 1


# Reposta para 'Como você entrou pra guilda?' (Linha 81)


def dialogo_extra3():
    print('\nKatrina: Sabe como é, depois de muito tempo no mar, você fica entediada dessa rotina, então eu saí! Claro,'
          ' ainda tô colada com um pessoal\nmeio barra pesada, mas isso tá no sangue')

    return 2

# -----------------------------------------------------------------------------------------------------------------------
