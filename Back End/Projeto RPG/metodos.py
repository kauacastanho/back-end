def esperar():

    input('')

def resposta(lista_respostas: list, pcena1, pcena2=0, pcena3=0):
    numero = 1
    for x in lista_respostas:
        print(f"{numero}: {x}")
        numero += 1
    cena_seguinte = input("")

    if pcena2 == 0:
        while cena_seguinte != '1':
            print("Por favor, digite um dos números indicados.")
            numero = 1
            for x in lista_respostas:
                print(f"{numero}: {x}")
                numero += 1
            cena_seguinte = input("")
        if cena_seguinte == '1':
            return pcena1()

    elif pcena3 == 0:
        while cena_seguinte != '1' and cena_seguinte != '2':
            print("Por favor, digite um dos números indicados.")
            numero = 1
            for x in lista_respostas:
                print(f"{numero}: {x}")
                numero += 1
            cena_seguinte = input("")
        if cena_seguinte == '1':
            return pcena1()
        elif cena_seguinte == '2':
            return pcena2()
    else:
        while cena_seguinte != '1' and cena_seguinte != '2' and cena_seguinte != '3':
            print("Por favor, digite um dos números indicados.")
            numero = 1
            for x in lista_respostas:
                print(f"{numero}: {x}")
                numero += 1
            cena_seguinte = input("")
        if cena_seguinte == '1':
            return pcena1()
        if cena_seguinte == '2':
            return pcena2()
        if cena_seguinte == '3':
            return pcena3()
