import sqlite3

class Banco:
    """classe para gerenciar as conexões com o banco de dados"""
    def __init__(self, nome_banco:str='agenda.db'):
        # na instanciação da classe, cria a conexão e o cursor com o banco
        self.con = sqlite3.connect(nome_banco)
        self.cur = self.con.cursor()

    def executa(self, query, parametros:tuple|None=None) -> None:
        """função para realizar as execuções das queries no banco de dados"""
        if parametros:
            self.cur.execute(query, parametros)
        else:
            self.cur.execute(query)

    def grava_disco(self) -> None:
        """salva as alterações no banco de dados do disco"""
        self.con.commit()

    def resgata(self, todos:bool=True) -> list|tuple:
        """quando é realizado o execute do cursor, se for SELECT, ainda precisa
        resgatar o que foi executado com a query;
        pode escolher entre retornar vários registros ou retornar apenas um"""
        if todos:
            # retorna uma lista de tuplas
            return self.cur.fetchall()
        else:
            # retorna apenas uma tupla
            return self.cur.fetchone()

    def cria_tabela(self) -> None:
        """função para executar a criação da tabela usada no banco de dados"""
        query:str = """CREATE TABLE IF NOT EXISTS AGENDA (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            endereco TEXT,
            telefone TEXT
        )
        """
        self.executa(query)
        self.grava_disco()

    def __del__(self):
        """como toda a conexão precisa ser fechada, quando se destruir o objeto
        instanciado já vai fechar a conexão"""
        self.con.close()

class Agenda:
    """classe para controlar a agenda; ela terá um atributo que realizará as
    conexões e quries com o banco de dados"""
    def __init__(self):
        """quando um objeto do tipo agenda for instanciado, ele vai se conectar
        através do atributo banco, vai criar a tabela e também já vai buscar
        todos os contatos existentes na tabela AGENDA"""
        self.banco:Banco = Banco()
        self.contatos:list = []
        self.banco.cria_tabela()
        self.busca_contatos()

    def cria_contato(self) -> None:
        """método usado quando se quer inserir um novo contato na AGENDA"""
        novo:Contato = Contato.novo_contato()
        query:str = """INSERT INTO AGENDA (nome, endereco, telefone) 
            VALUES (?,?,?)"""
        self.banco.executa(query,novo.cria_tupla())
        self.banco.grava_disco()
        self.contatos.append(novo)

    def busca_contatos(self) -> None:
        """busca todos os contatos na tabela AGENDA"""
        query:str = 'SELECT nome, endereco, telefone FROM AGENDA'
        self.banco.executa(query)
        lista:list = self.banco.resgata()

        self.contatos:list = []
        for item in lista:
            novo:Contato = Contato(item[0], item[1], item[2])
            self.contatos.append(novo)

    def busca_um(self) -> None:
        """busca apenas um contato, a critério do usuário"""
        query:str = 'SELECT * FROM AGENDA WHERE id=?'
        print('Digite o id do contato que quer buscar!')
        id:str = input(' >> ')
        self.banco.executa(query, (id,))
        buscado:tuple = self.banco.resgata(False)
        # aqui ainda dá para converter o contato buscado no banco em um objeto
        # do tipo contato e então exibir ele apropriadamente
        print(buscado)

    def lista_contatos(self) -> None:
        """lista todos os contatos presentes no atributo contatos"""
        for contato in self.contatos:
            print(contato)

    def __del__(self):
        """quando apagar o objeto do tipo agenda, também também apaga o objeto
        do tipo banco, fechando assim a conexão com o banco"""
        del self.banco

class Contato:
    """classe para gerenciar todos os contatos da agenda; cada contato de lá
    vai ser um objeto dessa classe"""
    def __init__(self, no:str, en:str, te:str):
        self.nome:str = no
        self.endereco:str = en
        self.telefone:str = te

    def cria_tupla(self) -> tuple:
        """quando se salva algum contato no banco de dados, é preciso passar
        uma tupla com os dados dele, então esse método é responsável por
        converter os atributos do objeto em uma tupla"""
        return (self.nome, self.endereco, self.telefone)

    def __str__(self):
        return f'Dados: {self.nome} - {self.endereco} - {self.telefone}.'

    @classmethod
    def novo_contato(cls):
        """método para ser chamado quando se quer pegar os dados de um novo
        contato do usuário, ele será chamado por um objeto do tipo agenda e
        então retornar um objeto do tipo Contato para ser salvo na lista de
        contatos"""
        print('Digite os dados do novo contato!\n')
        nome:str = input('Nome : ')
        endereco:str = input('Endereco : ')
        telefone:str = input('Telefone : ')
        return Contato(nome, endereco, telefone)

if __name__ == '__main__':
    agenda:Agenda = Agenda()
    agenda.lista_contatos()
    agenda.busca_um()
    # desafio: implementar a atualizacao e remocao de algum contato da agenda
    # e realizar uma busca com filtro
    del agenda

