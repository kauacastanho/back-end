from datetime import datetime
import sqlite3


class DB:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.setup_tables() 


    def setup_tables(self): #cria as tabelas restaurantes e produtos
        from main import CadastroRestaurante
        from main import PainelRestaurante
        cur = self.connection.cursor()
    
        cur.execute('''
            CREATE TABLE IF NOT EXISTS restaurantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                comissao TEXT NOT NULL
        )
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_produto TEXT NOT NULL,
                preco_produto FLOAT NOT NULL,
                id_restaurante INTEGER NOT NULL,
                FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
        )   
        ''')

        self.connection.commit()


    def create_produto(self, nome_produto, preco_produto, id_restaurante): #insere o produto na tabela produtos
        from main import PainelRestaurante
        
        cur = self.connection.cursor()
        cur.execute('''
            INSERT INTO produtos (nome_produto, preco_produto, id_restaurante) VALUES (?, ?, ?)
        ''', (nome_produto, preco_produto, id_restaurante))
        
        self.connection.commit()


    def create_restaurante(self, nome, email, senha, comissao): #insere os dados do restaurante na tabela restaurante
        from main import CadastroRestaurante

        cur = self.connection.cursor()
        cur.execute('''
            INSERT INTO restaurantes (nome, email, senha, comissao) VALUES (?, ?, ?, ?)
        ''', (nome, email, senha, comissao))
        
        self.connection.commit()


    def get_login_restaurante(self, email, senha): #verifica se existe o email e a senha do usuario para fazer login
        from main import CadastroRestaurante

        cur = self.connection.cursor()
        cur.execute('''
            SELECT id, nome, email, senha, comissao
            FROM restaurantes
            WHERE email = ? AND senha = ?
        ''', (email, senha))

        record = cur.fetchone()
        
        self.connection.commit()
        
        if record is None: #se nao existir retorna None
            return None

        return { #retorna todas as informaçõoes do restaurante
            'id': record[0],
            'nome': record[1],
            'email': record[2],
            'senha': record[3],
            'comissao': record[4],
        } 
        

    def get_restaurante_id(self, email): #retorna o id do restaurante
        cur = self.connection.cursor()
        cur.execute('''
            SELECT id FROM restaurantes WHERE email = ?
        ''', (email,))

        self.connection.commit()

        record = cur.fetchone()
        if record:
            return record[0] 
        else:
            return None


    def get_restaurante_email(self, email): #retorna o email do restaurante
        cur = self.connection.cursor()
        cur.execute('''
            SELECT email FROM restaurantes WHERE email = ?        
        ''',(email,))

        record = cur.fetchone()

        self.connection.commit()

        if record:
            return record[0]
        else: 
            return None


    def get_max_comissao(self): #retorna a maior comissão
        cur = self.connection.cursor()
        cur.execute('''
            SELECT MAX(comissao) FROM restaurantes
        ''',)

        record = cur.fetchone()

        self.connection.commit()

        if record:
            return record[0]
        else: 
            return None
    

    def get_current_comissao(self, email): #retorna a comissao atual
        
        cur = self.connection.cursor()
        cur.execute('''
            SELECT comissao FROM restaurantes WHERE email = ?
        ''',(email,))

        record = cur.fetchone()
        if record:
            return record[0]
        else: 
            return None
        
        self.connection.commit()


    def alter_comissao(self, update_comissao, email): #altera a comissão

        cur = self.connection.cursor()
        cur.execute('''
            UPDATE restaurantes
            SET comissao = ?
            WHERE email  = ? 
        ''',(update_comissao, email))
        
        self.connection.commit()


    def get_lista_produtos(self, id_restaurante): #retorna a lista de produtos do restaurante
        cur = self.connection.cursor()
        cur.execute('''
            SELECT id, nome_produto, preco_produto FROM produtos WHERE id_restaurante = ?        
        ''', (id_restaurante,))

        record = cur.fetchall()

        self.connection.commit()

        if record:
            produtos = []  #inicializa uma lista de produtos
            for row in record: #itera sobre cada linha de cada protudo do restaurante
                produto = {
                    'id': row[0],
                    'nome_produto': row[1],
                    'preco_produto': row[2]
                }
                produtos.append(produto)  #adiciona o produto na lista
            return produtos  
        else: 
            return None #se o restaurante não tiver nenhum produto retorna None


    def get_id_to_delet_prduct(self, id_restaurante): #retorna o id do produto

        cur = self.connection.cursor()
        cur.execute('''
            SELECT id FROM produtos WHERE id_restaurante = ?        
        ''', (id_restaurante,))

        record = cur.fetchall()

        self.connection.commit()

        if record:
            return record  
        else: 
            return None


    def delete_produto(self, delete): #deleta o produto
        cur = self.connection.cursor()

        cur.execute('''
            DELETE FROM produtos WHERE id = ?  
        ''',(delete,))

        self.connection.commit()


