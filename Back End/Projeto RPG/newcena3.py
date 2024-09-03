from metodos import esperar, resposta
from dicionario_de_respostas_v2 import dicionario_respostas


def cena3():
    print('\n[CENA 3 - CASA DOS ANDERSON]\n')
    esperar()
    print("\nO longo caminho cresce sobre seus olhos e a residência infinita assusta sua mente. "
          "A lua calmamente cai por trás dela, que cria uma enorme sombra de fim de dia.\n")
    esperar()
    print("O som do relincho fica mais baixo quanto mais próximo das luxuosas portas. "
          "A aldrava dourada com uma águia entalhada te encara com um olhar de mil jardas.\n")
    esperar()
    print("Você utiliza a aldrava e antes mesmo da terceira batida, "
          "um mordomo, cabelos grisalhos, pele escura e bengala na mão, abre a porta para você.\n")
    esperar()
    print("Mordomo: Boa noite senhor. Sou o responsável pela casa durante a ausência do Sr Anderson. Posso ajudá-lo?\n")
    resposta(dicionario_respostas["Cena3"]["parte0"],
             cena3_1)


def cena3_1():
    print('Mordomo: Oh céus, outros desses…\n')
    esperar()
    print('O senhor é interrompido por um alto e ecoado grito vindo do andar superior. ')
    esperar()
    print('Das escadas a sua frente, um homem fardado desce as escadas com papéis nas mãos e um pano na outra. ')
    esperar()
    print('Ele exclama em um sotaque de fora de Vevalon:\n')
    esperar()
    print('???: INVISÍVEL! ELE SÓ PODE SER INVISÍVEL!!\n')
    esperar()
    print('O velho homem dá um passo à frente, indignado.\n')
    esperar()
    print('Mordomo: Senhor Garneux, faça o favor! Suas ideias mirabolantes já estão indo longe demais.')
    esperar()
    print('???: Você não entende, essas pirraças estão cada vez mais espertas! '
          'No quartel, elas roubavam espadas\n'
          'e vendiam para pilantras do Porto como se fosse farinha!! Devem ter encontrado algum tipo de pergaminho\n'
          'com uma magia de invisibilidade e roubaram vocês.')
    esperar()
    print('Mordomo: Você tentou usar algum tipo de detecção de magia?')
    esperar()
    print('???: Sim!')
    esperar()
    print('Mordomo: E encontrou algo?')
    esperar()
    print('???: Não… eu vou pensar em algo. E você?\n')
    esperar()
    print('O rapaz te olha com certo desdém, tentando entender sua desconfortável presença. O olhar te sonda,\n'
          'suas vestes talvez entreguem que é membro da guilda ou um camponês realmente enfurecido.')
    esperar()
    resposta(dicionario_respostas["Cena3"]["parte1"],
             cena3_2,
             cena3_3)


def cena3_2():
    print('???: Agradeço o entusiasmo, mas não preciso de ajuda! Eu estou a um triz de encontrar esse maldito\n'
          'que está importunando a família Anderson mais uma vez!')
    esperar()
    resposta(dicionario_respostas["Cena3"]["parte2"],
             cena3_21,
             cena3_22)


def cena3_3():
    print('???: Motivado, gostei. Bem, fica a vontade procurando o segundo andar,'
          ' eu já cuidei daqui de baixo e do cofre. \n'
        'Vou olhar o sótão e… o quarto dos funcionários…')
    esperar()
    print('Marceu lança um olhar assassino para o mordomo, que dá de ombros para o mesmo.')
    print('Beleza, mas antes...')
    resposta(dicionario_respostas["Cena3"]["parte3"],
             cena3_41,
             cena3_42,
             cena3_43)


def cena3_21():
    print('???: Quanta astúcia de sua parte, aventureiro. Bem, vai para o segundo andar que eu vou cuidar do sótão. \n'
          'Se avistar alguma coisa, me avise, sim?')
    esperar()
    print('Claro, mas antes...')
    esperar()
    resposta(dicionario_respostas["Cena3"]["parte3"],
             cena3_41,
             cena3_42,
             cena3_43)


def cena3_22():
    print('???: Você é grosseiro demais para um defensor dos direitos civis igual a mim, aventureiro. \n'
          'Vai para o segundo andar que eu dou um jeito no que falta, sim? E me chame caso seja extremamente necessário'
          )
    esperar()
    print('OK, mas antes...')
    esperar()
    resposta(dicionario_respostas["Cena3"]["parte3"],
             cena3_41,
             cena3_42,
             cena3_43)


def cena3_41():
    print('Marceu Garneux: Tenente Marceu Garneux, ao seu dispor. '
          'Sou um dos diplomatas da guilda e um dos… investigadores? \n'
          'Eu não sei muito bem qual posto a Mayla me pôs nos últimos meses, mas isso que eu tenho feito.')
    esperar()

    dicionario_respostas['Cena3']['parte3'].remove("Quem é você mesmo?")

    if len(dicionario_respostas["Cena3"]["parte3"]) == 2:
        resposta(dicionario_respostas["Cena3"]["parte3"],
                 cena3_42,
                 cena3_43)
    elif len(dicionario_respostas["Cena3"]["parte3"]) == 1:
        if dicionario_respostas["Cena3"]["parte3"][0] == "Você disse quartel… você serviu?":
            resposta(dicionario_respostas["Cena3"]["parte3"],
                     cena3_42)
        elif dicionario_respostas["Cena3"]["parte3"][0] == "Como você entrou na Guilda?":
            resposta(dicionario_respostas["Cena3"]["parte3"],
                     cena3_43)
    elif len(dicionario_respostas["Cena3"]["parte3"]) == 0:
        cena3_5()


def cena3_42():
    if dicionario_respostas['Cena3']['parte3'][0] == "Quem é você mesmo?":
        print(
            '???: Ah sim, eu servi! Desde meus 14 anos eu sirvo ao exército de Puphitia,'
            ' apesar de ser nascido em Vevalon.')
        esperar()
        print(
            'Você queima alguns neurônios para se lembrar e realmente funciona,'
            ' Puphitia é um reino vizinho de Vevalon, \n'
            'na região Oeste do Continente. Ele se estende por toda uma floresta,'
            ' abrigando todos as principais raças que '
            'vem de lá\n'
            ' (elfos, fadas, centauros, gnomos…)')
        esperar()
        print('???: Liderei um batalhão durante a guerra contra os monges do sul. Bons tempos…”')
    else:
        print(
            'Marceu Garneux: Ah sim, eu servi! Desde meus 14 anos eu sirvo ao exército de Puphitia,'
            ' apesar de ser nascido em Vevalon.')
        esperar()
        print(
            'Você queima alguns neurônios para se lembrar e realmente funciona,'
            ' Puphitia é um reino vizinho de Vevalon, \n'
            'na região Oeste do Continente. Ele se estende por toda uma floresta,'
            ' abrigando todos as principais raças que '
            'vem de lá\n'
            ' (elfos, fadas, centauros, gnomos…)')
        esperar()
        print('Marceu Garneux: Liderei um batalhão durante a guerra contra os monges do sul. Bons tempos…”')
    esperar()

    dicionario_respostas['Cena3']['parte3'].remove("Você disse quartel… você serviu?")

    if len(dicionario_respostas["Cena3"]["parte3"]) == 2:
        resposta(dicionario_respostas["Cena3"]["parte3"],
                 cena3_41,
                 cena3_43)
    elif len(dicionario_respostas["Cena3"]["parte3"]) == 1:
        if dicionario_respostas["Cena3"]["parte3"][0] == "Quem é você mesmo?":
            resposta(dicionario_respostas["Cena3"]["parte3"],
                     cena3_41)
        elif dicionario_respostas["Cena3"]["parte3"][0] == "Como você entrou na Guilda?":
            resposta(dicionario_respostas["Cena3"]["parte3"],
                     cena3_43)
    elif len(dicionario_respostas["Cena3"]["parte3"]) == 0:
        cena3_5()


def cena3_43():
    if dicionario_respostas['Cena3']['parte3'][0] == "Quem é você mesmo?":
        print('???: Depois de muitos anos e algumas feridas que não se fecharam corretamente, acho que \n'
              'tá na hora de sair das grandes batalhas e enfrentar algo menos… grandioso, apesar de estar fora '
              'do meu padrão.')
    else:
        print('Marceu Garneux: Depois de muitos anos e algumas feridas que não se fecharam corretamente, acho que \n'
              'tá na hora de sair das grandes batalhas e enfrentar algo menos… grandioso, apesar de estar fora '
              'do meu padrão.')
    esperar()

    dicionario_respostas['Cena3']['parte3'].remove("Como você entrou na Guilda?")

    if len(dicionario_respostas["Cena3"]["parte3"]) == 2:
        resposta(dicionario_respostas["Cena3"]["parte3"],
                 cena3_41,
                 cena3_42)
    elif len(dicionario_respostas["Cena3"]["parte3"]) == 1:
        if dicionario_respostas["Cena3"]["parte3"][0] == "Quem é você mesmo?":
            resposta(dicionario_respostas["Cena3"]["parte3"],
                     cena3_41)
        elif dicionario_respostas["Cena3"]["parte3"][0] == "Você disse quartel… você serviu?":
            resposta(dicionario_respostas["Cena3"]["parte3"],
                     cena3_42)
    elif len(dicionario_respostas["Cena3"]["parte3"]) == 0:
        cena3_5()


def cena3_5():
    print('Marceu Garneux: Mas chega de enrolação! Temos um roubo para solucionar um ladrão para prender. '
        'Vai logo para o segundo andar!')
    esperar()
    print('Talvez a contragosto, talvez empolgado, '
        'você começa a seguir em direção das escadarias que crescem sobre sua cabeça. \n'
        'Seu primeiro caso está chegando em algo interessante! Ou algo assustador…')

