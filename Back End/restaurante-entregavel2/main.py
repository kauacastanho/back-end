
from database.db import DB  

import re 
import os


class Utils: 
    @staticmethod
    def clear_screen(): #função estática que limpa a tela
        os.system('cls' if os.name == 'nt' else 'clear')


class TelaInicial:

    def __init__(self):  
        while True:  
            try: 
                opcao_inicial = int(input("\n1. Cadastrar Restaurante\n2. Fazer Login \n")) #solicita um numero
                if opcao_inicial in (1, 2): #se o numero for válido sai do loop 
                    break 
                else:
                    print("Opção Inválida, Digite Novamente.\n")
            except ValueError: # se o usuario digitar qualquer outra coisa que não seja um numero imprime: 
                print("Entrada inválida. Por favor, digite um número.")

        self.opcao_inicial = opcao_inicial #armazena a opcao escolhida
        Utils.clear_screen() 


class CadastroRestaurante:

    def __init__(self, opcao_inicial, my_db):
        
        self.validador = Validador() #inicializa a classe validador

        nome = input('\nDigite o nome do restaurante: ')
        self.nome = self.validador.valida_nome(nome) #valida o nome
        

        email = input('\nDigite seu email: ')
        self.email = self.validador.valida_email(email, my_db) #valida email
       
        senha = input('\nDigite sua senha: ')
        self.senha = self.validador.valida_senha(senha)  #valida a senha
        
        self.maior_comissao() #chama a função maior_comissao
        comissao = input('\nDigite o valor da comissão (%): ')
        self.comissao = self.validador.valida_comissao(comissao) #valida a comissão
        
        my_db.create_restaurante(self.nome, self.email, self.senha, self.comissao) #manda as informações para o banco
        Utils.clear_screen()
        print(f'\nO restaurante {nome} foi criado!\n\nFaça Login para entrar. ')
        
        
    def maior_comissao(self): #imprime a maior comissao registrada
        if my_db.get_max_comissao() is None:
            print("\nNão foi cadastrado nenhuma comissão até o momento.")
        else:
            print(f'\nA maior comissão é de {int(my_db.get_max_comissao())}%')


class Validador:

    def valida_nome(self, nome):
        padrao_nome = r'^[A-Za-zÀ-ÿ\s]{10,}$' #define o padrao do nome
        while not re.match(padrao_nome, nome): #enquanto nome nao se encaixar no padrao, solicita uma nova entrada
            nome = input("\nNome inválido. Digite novamente:  ")
        return nome #retorna o nome


    def valida_email(self, email, my_db):
        self.my_db = my_db

        padrao_email = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{3,}+$' #define o padrao do email
        
        while True:
            if not re.match(padrao_email, email): #enquanto email nao se encaixar no padrao, solicita uma nova entrada
                email = input("\nEmail inválido. Digite novamente: ")
                continue

            if my_db.get_restaurante_email(email) is not None: #verifica se o email ja existe no banco
                email = input("\nEmail já existente. Digite outro: ")
            else:
                break

        email = email.lower() 
        return email #retorna o email em lower case


    def valida_senha(self, senha):
        padrao_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{5,}$' #define o padrao da senha
        while not re.match(padrao_senha, senha): #enquanto senha nao se encaixar no padrao, solicita uma nova entrada
            print('\nSenha inválida.\nSua senha deve conter pelo menos 1 letra maiúscula, 1 letra minúscula, 1 número e ter no mínimo 1 caracter\n') 
            senha = input("Digite novamente: ")
        return senha #retorna a senha


    def valida_comissao(self, comissao):
        while True:
            try:
                valor_comissao = int(comissao) 
                if valor_comissao > 0:
                    return valor_comissao #se o usuario digitou um  numero maior que zero, retorna a comissao
            except ValueError: #se o usuario nao digitou um numero, solicita uma nova entrada 
                comissao = input("\nComissão inválida. Digite novamente: ")
        

class Login:

    def __init__(self, opcao_inicial, my_db):
        self.opcao_inicial = opcao_inicial #inicializa o construtor
        self.my_db = my_db
        self.painel_restaurante = None  

    def realizar_login(self):
        email = input('\nDigite seu email: ').strip().lower() #solicita email, senha
        senha = input('\nDigite sua senha: ').strip()
        
        resultado = self.my_db.get_login_restaurante(email, senha) #verifica o login e retorna todas as colunas do cadastro

        if resultado is None: #se o email ou senha estiver incorreto: 
            print("\nLogin Incorreto")
            return False  
        else:
            Utils.clear_screen()
            print(f"\nBem-vindo, {resultado['nome']}!")

            self.restaurante_id = self.my_db.get_restaurante_id(email)  # obtendo o ID do restaurante
            self.painel_restaurante = PainelRestaurante(self.restaurante_id, my_db, email) #inicializa o PainelRestaurante
            
            return True  


class PainelRestaurante:

    def __init__(self, restaurante_id, my_db, email):
        self.restaurante_id = restaurante_id
        self.my_db = my_db
        self.email = email
        self.lista_produtos = self.my_db.get_lista_produtos(self.restaurante_id) #puxa a lista de produtos

        if self.lista_produtos: #imprime os produtos se tiver
            print("\nProdutos Cadastrados: \n")
            for produto in self.lista_produtos: 
                print(f"ID: {produto['id']} | Nome: {produto['nome_produto']} | Preço: R${produto['preco_produto']:.2f}") #formata os produtos
        else: 
            print("\nNenhum produto cadastrado!")


        while True:
            try:
                opcao_painel = int(input("\n1. Cadastrar produto\n2. Deletar produto\n3. Alterar comissão\n4. Logout\n")) #solicita um numero
                if opcao_painel in (1, 2, 3, 4): #se o numero for um destes
                    break #sai do loop
                else:
                    print("\nOpção Inválida, Digite Novamente.\n") #se nao, imprime: 
            except ValueError: #se o usuario digitar outro caracter imprime: 
                print("\nEntrada inválida. Por favor, digite um número.")
        self.opcao_painel = opcao_painel #armazena a opcao 
        self.envia_opcao(self.opcao_painel, restaurante_id) #chama o metodo envia_opcao


    def envia_opcao(self, opcao_painel, restaurante_id):

        self.opcao_painel = opcao_painel 

        
        if  opcao_painel == 1: #se a opcao for 1 chama a funcao cadastrar_produto
            Utils.clear_screen()
            self.cadastrar_produto()
        elif opcao_painel == 2: #se a opcao for 2 chama a funcao apagar_produto
            Utils.clear_screen()
            self.apagar_produto()
        elif opcao_painel == 3: #se a opcao for 3 chama a funcao alterar_comissao
            Utils.clear_screen()
            self.alterar_comissao()
        elif opcao_painel == 4: #se a opcao for 4 chama a funcao fazer_logout
            Utils.clear_screen()
            self.fazer_logout()
        
    def cadastrar_produto(self):


        nome_produto = input('\nDigite o nome do produto: ') 
        self.nome_produto = self.valida_nome_produto(nome_produto) #chama o validador que retorna o poduto

        preco_produto = input('\nDigite o preço do produto: ')
        self.preco_produto = self.valida_preco_produto(preco_produto) #chama o validador que retorna o preco

        my_db.create_produto(self.nome_produto, self.preco_produto, self.restaurante_id) #insere o produto na tabela produtos
        print(f'\nProduto {nome_produto} cadastrado com sucessso!')
        input("\nDigite enter para prosseguir: ")
        Utils.clear_screen()

        self.painel_restaurante = PainelRestaurante(self.restaurante_id, self.my_db, self.email) #volta para o painel

    def valida_nome_produto(self, nome_produto): #funcao que valida o nome do produto e retorna o produto
        padrao_nome_produto = r'^[A-Za-zÀ-ÿ\s]{6,}$' 
        while not re.match(padrao_nome_produto, nome_produto):
            nome_produto = input("\nNome inválido. Digite novamente:  ")
        return nome_produto

    def valida_preco_produto(self, preco_produto): #funcao que valida o preco do produto e retorna o preco
        padrao_preco_produto = r'^(0|[1-9]\d*)(\.\d+)?$'
        while not re.match(padrao_preco_produto, preco_produto):
            preco_produto = input("\nPreço inválido. Digite novamente:  ")
        return preco_produto

    def apagar_produto(self):
        if self.lista_produtos: #se existir produto cadastrado
            print("\nProdutos Cadastrados: \n")
            for produto in self.lista_produtos: #imprime os produtos formatados 
                print(f"ID: {produto['id']} | Nome: {produto['nome_produto']} | Preço: R${produto['preco_produto']:.2f}")
        else: #se nao tiver produto cadastrado volta para o painel
            self.painel_restaurante = PainelRestaurante(self.restaurante_id, self.my_db, self.email)
        
        self.select_product_to_delet() #chama a funcao para deletar
        self.painel_restaurante = PainelRestaurante(self.restaurante_id, self.my_db, self.email) #volta para o painel

    def select_product_to_delet(self):
        if self.lista_produtos:
            ids_disponiveis = [] #inicializa uma lista
            for produto in self.lista_produtos: #itera por cada produto na lista 
                ids_disponiveis.append(produto['id']) #adiciona os ids na lista
        else: 
            print("\nNenhum produto cadastrado!")
            self.__init__()

        while True:
            try: 
                delet = input("\nDigite ID do produto que deseja deletar: ") 

                delet = int(delet)


                if delet in ids_disponiveis:
                    my_db.delete_produto(delet) #deleta o produto no banco
                    print("\nProduto Deletado com sucesso!")
                    input("\nAperte enter para prosseguir: ")
                    Utils.clear_screen()
                    break
                else: #se a entrada for invalida: 
                    print("\nID Inválida. Tente Novamente.\n")
            except ValueError:
                print("\nEntrada inválida. Por favor, digite um número.")

    def alterar_comissao(self):
        print(f'\nSua comissão atual é de {int(self.my_db.get_current_comissao(self.email))}%') #imprime a comissao atual
        
        update_comissao = input("\nDigite sua nova comissão: ")
        
        while True:
            try:
                update_comissao = int(update_comissao)
                if update_comissao > 0: #se a nova comissao for maior que 0, sai do loop
                    break
                else: #se nao imprime: 
                    update_comissao = input("\nComissão inválida. Digite novamente: ") 
            except ValueError:
                update_comissao = input("\nComissão inválida. Digite novamente: ")
        
        self.my_db.alter_comissao(update_comissao, self.email) #altera a comissao no banco
        print("\nComissão atualizada com sucesso!")
        input("\nAperte enter para prosseguir: ")
        Utils.clear_screen()

        self.painel_restaurante = PainelRestaurante(self.restaurante_id, self.my_db, self.email) #volta para o painel

    def fazer_logout(self):
        
        self.restaurante_id = None #zera a variavel que contem a funcao
        return True  
            

if __name__ == '__main__':
    Utils.clear_screen()
    my_db = DB('database.db') #define a classe DB
    
    while True:
        iniciar = TelaInicial() #chama a funcao tela inicial
        
        if iniciar.opcao_inicial == 1: #se a opcao inicial for 1: 
            CadastroRestaurante(iniciar.opcao_inicial, my_db) #chama a classe cadastro restaurante
        elif iniciar.opcao_inicial == 2: #se a opcao for 2:
            login_instance = Login(iniciar.opcao_inicial, my_db) #chama a classe login
        
            while True: 
                if login_instance.realizar_login():
                    # chama o painel apenas se o login for bem-sucedido
                    while login_instance.painel_restaurante is not None: #se o login for not None 
                        
                        if login_instance.painel_restaurante.fazer_logout():
                            break  # retorna para tela inicial
                else:
                    print("Por favor, tente fazer login novamente.") 
                       