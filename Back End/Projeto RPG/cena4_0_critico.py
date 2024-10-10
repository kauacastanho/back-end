import random


def esperar():
    input("")


def determina_vercedor(acao_jogador, acao_inimigo):
    if (acao_jogador == "ataque" and acao_inimigo == "defesa"):
        print(
            '\nVocê levanta sua espada em guarda para atacar a criatura e ela, um pouco mais rápida que você,\n'
            'dá um passo ao lado e sua espada acerta o chão.')
        esperar()
        return "inimigo"
    elif (acao_jogador == "defesa" and acao_inimigo == "ataque"):
        print(
            '\nVocê vê o pequeno kobold vindo com as garras em sua direção e, no último instante,\n'
            'você usa sua espada para aparar o ataque e fugir do corte.')
        esperar()
        return 'jogador'
    elif (acao_jogador == "ataque" and acao_inimigo == "magia"):
        print(
            '\nVocê vai fazer um corte na lateral do corpo do seu inimigo'
            ' e nota uma pequena bola flamejante se formando em sua mão.\n'
            'Instantes antes dele jogar aquilo em sua direção, você acerta seu braço e nega o ataque do oponente.')
        esperar()
        return 'jogador'
    elif (acao_jogador == "magia" and acao_inimigo == "ataque"):
        print(
            '\nDe forma desesperada, você começa a preparar uma lâmina de gelo para atingir ele,'
            ' mas quando vai mirar, não enxerga seu alvo. O fato é que ele já está abaixo de ti,\n'
            'cortando sua canela com suas longas unhas.')
        esperar()
        return 'inimigo'
    elif (acao_jogador == "magia" and acao_inimigo == "defesa"):
        print(
            '\nA pobre criatura tenta cruzar os braços em defensiva,'
            ' mas sua faca de gelo é mais rápida e atinge no meio de seu estômago,\n'
            'o congelando por um segundo, mas logo cortando o efeito.')
        esperar()
        return 'jogador'
    elif (acao_jogador == "defesa" and acao_inimigo == "magia"):
        print(
            '\nVocê vai utilizar sua espada para bloquear, mas é inevitável,'
            ' o fogo esquenta o metal de sua arma até o cabo,\n'
            'queimando suas mãos.')
        esperar()
        return 'inimigo'
    elif (acao_jogador == "ataque" and acao_inimigo == "ataque"):
        print(
            '\nOs dois se lançam para cima um do outro para um ataque e, ferozmente,'
            ' começam a se digladiar com ataques desengonçados.\n'
            ' Ambos param quando notam que nenhum dos dois está acertando seu alvo.')
        esperar()
        return 'empate'
    elif (acao_jogador == "magia" and acao_inimigo == "magia"):
        print(
            '\nOs dois param durante um segundo para poder pensar no próximo ato e,'
            ' de forma síncrona, os dois conjuram e lançam suas respectivas magias,\n'
            'que se chocam e se negam no meio do caminho.')
        esperar()
        return 'empate'
    else:
        print(
            '\nOs dois começam a se rodear de forma defensiva,'
            ' rodando pelo quarto com medo da próxima ação de seu oponente.\n'
            'Um movimento deve ser feito de imediato.')
        esperar()
        return 'empate'


def combate():
    acoes = ["ataque", "defesa", "magia"]
    vidas_jogador = 10
    vidas_inimigo = 6
    print('[Combate]')
    esperar()
    print(
        'Atacar: O ataque sempre será mais rápido que uma conjuração, mas previsível demais para não ser contra-atacado.\nVence da magia, perde para defesa.')
    esperar()
    print(
        'Defender: Defender é ótimo contra ataques corpo a corpo, mas inevitável para magias.\nVence do Atacar, perde para magia.')
    esperar()
    print(
        'Conjurar Magia: Magia é lenta, mas eficiente contra quem não te ataca.\nPerde para Atacar, vence para defesa.')
    esperar()
    print(f"\n> Vida: {vidas_jogador}/10")
    print("1. Atacar \n2. Defender  \n3. Conjurar Magia")

    while vidas_jogador > 0 and vidas_inimigo > 0:
        while True:
            escolha_jogador = input("Escolha sua ação (1-3): ")
            if escolha_jogador == '1' or escolha_jogador == '2' or escolha_jogador == '3':
                break
            else:
                print("Por favor, digite um dos números indicados.")

        escolha_jogador = (int(escolha_jogador) - 1)

        acao_jogador = acoes[escolha_jogador]
        acao_inimigo = random.choice(acoes)

        vencedor = determina_vercedor(acao_jogador, acao_inimigo)

        if vencedor == "empate":
            print("Nada acontece.")
            esperar()
        elif vencedor == "jogador":
            dano_causado = random.choice([1, 2, 2, 2, 4])
            print(f"O inimigo perde {dano_causado} vida.")
            if dano_causado == 1:
                print("O golpe não acertou em com força.")
            elif dano_causado == 4:
                print("O golpe acertou em cheio!")
            esperar()
            vidas_inimigo -= dano_causado
        else:
            dano_causado = random.choice([1, 2, 2, 2, 4])
            print(f"Você perde {dano_causado} vida.")
            if dano_causado == 1:
                print("O golpe não acertou em com força.")
            elif dano_causado == 4:
                print("O golpe acertou em cheio!")

            esperar()
            vidas_jogador -= dano_causado

        if vidas_jogador > 0 and vidas_inimigo > 0:
            print(f"> Vida: {vidas_jogador}/10")
            print("1. Atacar \n2. Defender  \n3. Conjurar Magia")

    if vidas_jogador > 0:
        print("\nVocê venceu!\n")

        return True
    else:
        print("\nVocê perdeu!\n")

        return False


def escolha1():
    print("\nVocê saca sua arma e, com um súbito movimento, você entra no quarto e golpeia o vento.")
    esperar()

    print("Após escanear a sala, tenta conjurar a magia “revelar oculto”, mas nada.")
    esperar()

    print("O olhar para fora da janela, um frio sobe sua espinha rapidamente.")
    esperar()

    print('Olhar aquele labirinto de arbustos altos não ajuda, mas também a desconfortável '
          'presença de um outro ser dentro desse cômodo incomoda ainda mais.')
    esperar()

    print("Somente uma janela aberta, com as cortinas voando e batendo contra a parede.")
    esperar()

    print("Você não encontra mais nada.")


def escolha2():
    print('\nA angústia volta a te tomar quanto mais próximo da porta você chega e, '
          'com um encontrão do seu ombro na madeira,\n'
          'você não vê nada mais além de uma vela acesa no candelabro, na escrivaninha do quarto.')
    esperar()

    print('Chegando mais perto, você vê uma pilha de papéis com o que parece ser estudo '
          'sobre criaturas não sencientes ou pouco sencientes.')
    esperar()

    print("Os principais resultados envolvem Kobolds, orcs, goblins e elementais.")
    esperar()

    print('É estranho esse tipo de estudo vindo de pessoas da alta classe, mas quem é '
          'você para julgar? Você decide sair do quarto.')


def escolha3():
    global combate_resultado
    print("\nA passos lentos, você se aproxima da porta mais longe do início do caminho. ")
    esperar()

    print('Parece incessante o ruído craquelado que sai do quarto, parecendo com mordidas '
          'em algo metálico ou amadeirado.')
    esperar()

    print("Você põe o olho na fechadura e, aparentemente, o que o Marceu disse não era tanta insanidade.")
    esperar()

    print("Você enxerga dentro do quarto aquele ovo flutuando, como se alguém estivesse o segurando.")
    esperar()

    print("Com uma única batida, você abre a porta já conjurando “revelar oculto”.")
    esperar()

    print('Uma criatura aos poucos começa a se tornar visível aos seus olhos. Um kobold, um '
          'ser pequeno e reptiliano começa a tentar esconder o ovo Fabergé com muito descuido')
    esperar()

    print("Kobold: SAI PRA LÁ, PANACA! EU ACHEI PRIMEIRO, #%&%!!")
    esperar()

    print("Por impulso, você saca sua arma e vai pra cima do kobold!")
    esperar()

    combate_resultado = combate()


#######################
#######COMBATE#########
#######################


def fim1():
    print('\nVocê coloca ele dentro de sua bolsa e joga o corpo do kobold '
          'pela janela, cobrindo seus rastros.')
    esperar()

    print("Marceu e Katrina entram correndo dentro de seu quarto, dizendo que ouviram uma luta.")
    esperar()

    print('Você diz que lutou com uma criatura, mas que estava escuro demais\n'
          'e ela te deixou inconsciente. ')
    esperar()

    print('Com a promessa perfeita de uma vida nova nas mãos, você volta até Kallista e,\n'
          'após um tempo de negociação, consegue fazer uma boa divisão com ela dos ganhos.')
    esperar()

    print("Com o silêncio de sua cúmplice comprado e o dinheiro em mãos, agora está livre!")
    esperar()

    print('Você sai pelos portões de Vevalon de barco, fugindo para os arredores de Puphitia,\n'
          'onde você consegue sua vida nova.')
    esperar()

    print('Uma fazenda, sua produção para consumo próprio, alguns amigos elfos e centauros e\n'
          'seu tesouro bem escondido.')
    esperar()

    print('Você ainda se pergunta se algum dia iriam atrás de você pelo que fez,\n'
          'mas a guilda tinha problemas maiores envolvendo seu próprio rei.')
    esperar()

    print('Apesar da angústia te devorar e o arrependimento do crime te consumir,\n'
          'sua vida segue tranquila e plena.')
    esperar()

    print("O tesouro é seu.")
    esperar()

    print("FIM! OBRIGADO POR JOGAR!")
    exit()


def fim2():
    print('\nApesar da tentação te engolir por um segundo, você não '
          'deixa ela vencer sua cabeça.')
    esperar()

    print('Atrás de você, Marceu e Kallista entram no quarto,\n'
          'esbaforidos, com medo de você ter se machucado seriamente.')
    esperar()

    print('Eles seguem seu dedo ensanguentado até a bolsa do kobold, '
          'onde eles recuperam em meio a gritos de comemoração,\no ovo '
          'Fabergé que tanto almejam.')
    esperar()

    print('Você, em sua primeira missão, desvendou um mistério que nem '
          'mesmo os cabeças da guilda conseguiram (ou tentaram)!')
    esperar()

    print("E você acaba sendo imensamente parabenizado por isso.")
    esperar()

    print('O seu nome é posto na parede de membros oficiais e, talvez '
          'pela primeira vez, você conseguiu um grupo inusitado de amigos!\n'
          'Marceu, Katrina e Kallista, o trio que anteriormente te ajudou, '
          'agora estão mais próximos que nunca.')
    esperar()

    print("O dinheiro com certeza não compensa, mas o renome te faz alguém mais leve.")
    esperar()

    print("Talvez ter ficado com o ovo te faria mais feliz? Talvez")
    esperar()

    print("Mas acho que nunca saberemos.")
    esperar()

    print("E você prefere assim.")
    esperar()

    print("A vida é mais leve assim.")
    esperar()

    print("FIM! OBRIGADO POR JOGAR!")
    exit()


# [CENA 4 - O ROUBO]

def cena_4():
    print('\n[CENA 4 - O ROUBO]\n')
    esperar()
    print("O corredor que você entra parece ser infinito. ")
    esperar()

    print('A lua no vitral cria uma sombra no chão no formato '
          'de Hamaliel, o rei de Vevalon.')
    esperar()

    print('Ele segura na mão direita um mangual com a cabeça '
          'brilhando em dourado e um enorme escudo na mão esquerda.')
    esperar()

    print('Um aasimar, descendente direto de anjo, com enormes asas '
          'brancas e uma armadura que reflete sua personalidade divina,\n'
          'no sentido literal.')
    esperar()
    opcoes1()


def opcoes1():
    fechar = False
    opcoes_disponiveis = ['1', '2', '3']
    while not fechar:

        print("\nEscolha uma das opções:")

        if '1' in opcoes_disponiveis:
            print("1: Checar a porta da corrente de ar")
        if '2' in opcoes_disponiveis:
            print("2: Checar a porta da luz")
        if '3' in opcoes_disponiveis:
            print("3: Checar a porta do som")

        while True:
            escolha = input("")
            if escolha in opcoes_disponiveis:
                break
            else:
                print("Por favor, digite um dos números indicados.")

        if escolha == '1':
            escolha1()
            opcoes_disponiveis.remove('1')
        elif escolha == '2':
            escolha2()
            opcoes_disponiveis.remove('2')
        elif escolha == '3':
            escolha3()
            fechar = True


def vitoria_ou_derrota():
    # combate_resultado = combate()

    if not combate_resultado:

        print("Você perdeu suas esperanças com o mundo ao ver sua vida se esvaindo pelos seus olhos.")
        esperar()
        print('Os últimos instantes que você poderia estar ouvindo aqueles que te amam declarar suas '
              'últimas palavras são tomados pelos risos do Kobold\n'
              'e o som da porta sendo arrebentada por Marceu e Katrina, que chegou enquanto você batalhava.')
        esperar()
        print("Talvez a missão tenha realmente sido concluída, mas a que custo?")
        esperar()
        print("Valeu entregar sua vida para uma cidade que te verá como mais um túmulo?")
        esperar()
        print("Perguntas demais para pouco tempo de vida.")
        esperar()
        print("No fim das contas, você sente que serviu de algo, ao menos uma lição.")
        esperar()
        print("Game Over.")
        while True:
            aux = input("Deseja tentar novamente?\n1. Sim\n2. Não\n > ")
            if aux == "2":
                print("OBRIGADO POR JOGAR!")
                break
            elif aux == "1":
                escolha3()
            else:
                print("Por favor, digite um dos números indicados..")

    elif combate_resultado:
        print('Você vê o corpo se enrijecendo e caindo sobre seus pés. A árdua batalha se deu por '
              'terminada e,\npor um triz, vencida. Isso nunca tiraria seu mérito, obviamente. ')
        esperar()
        print('Mas talvez o que você procura não seja o mérito ou a sua bondade em ajudar o próximo,\n'
              'mas o que todos nessa cidade querem. Crescer.')
        esperar()
        print('Você analisa o corpo e vê, dentro da pequena bolsa do Kobold,\no grande ovo Fabergé '
              'que tanto se fala dentro dessa casa.')
        esperar()
        print("Querendo ou não, aos olhos dos demais, ele ainda foi roubado e sumido.")
        esperar()
        print("Você tem a oportunidade de crescer na sua frente, mas sua índole permite?")
        esperar()
        print("Queres ser aquilo que outrora jurou exterminar?")

        opcoes2()


def opcoes2():
    print("\n1: Roubar o ovo")
    print("2: Entregar o ovo para a família\n")

    while True:
        escolha = input("")
        if escolha == '1':
            fim1()
        elif escolha == '2':
            fim2()
        else:
            print("Por favor, digite um dos números indicados.")


########## teste de combate ###########
#combate()