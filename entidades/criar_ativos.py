from sqlmodel import Session, select  # importa a biblioteca sqlmodel e seus métodos e classes
from banco_de_dados.base_dados import GestaoAtivos, engine # importa o módulo onde está o código do banco de dados, e o banco de dados
from decimal import Decimal # importa a biblioteca decimal, para números com casas decimais
from nota_fiscal.gerar_nota_fiscal import gerar_nota_fiscal # importa a função de gerar a nota fiscal
from funcoes_de_alteracao.alterar_dados import AlterarDados # importa a função que altera o status

class CriarAtivos:  # Cria uma classe que contém as funcionalidades do sistema
    

    
    def cadastrar(self, produto, descricao, valor, quantidade, status): # define o método para cadastro.
       
        with Session(engine) as session: # abre uma conexão no banco de dados.

            # configura os dados para serem salvos no banco de dados
            registrar_dados = GestaoAtivos(nota_fiscal=gerar_nota_fiscal(), produto=produto, descricao=descricao, valor=valor.quantize(Decimal('0.01')), quantidade=quantidade, status=status)
            session.add(registrar_dados) # prepara os dados para serem salvos no banco de dados
            session.commit() # envia os dados para o banco de dados
      


    def consultar(self, produto):  # define o método consultar
           
        with Session(engine) as session: # abre uma conhexão no banco de dados
            produto_consultado = select(GestaoAtivos).where(GestaoAtivos.produto == produto) # realiza uma consulta SQL na tabela Gestão ativos, e verifica se o paramentro é igual a variavel produto
            produto_consultado = session.exec(produto_consultado).first() # executa a consulta da linha anterior e pega o primeiro valor correspondente 
            
            return produto_consultado # retorna a consulta se ela for encontrada.
            

    
    
    def alterar(self, parametro, editar_produto=False, editar_descricao=False, editar_valor=False, editar_quantidade=False, editar_status=False): # define o método alterar, com os parametros que serão alterados.
        alterar_dados = AlterarDados() # instância a classe AlterarDados

        if editar_produto is True: #realiza uma ação se caso o usuário queira alterar o nome do produto, passamdo o editar_produto=True na chamada do método
            self.consultar(parametro) # chama o método consultar da classe.
            alterar_dados.alterar_nome_produto(parametro) # chama a classe e o método que faz a alteração do status.
        
        elif editar_descricao is True: #realiza uma ação se caso o usuário queira alterar a descrição, passando o editar_descricao=True na chamada do método 
            self.consultar(parametro) # chama o método consultar da classe.
            alterar_dados.alterar_descricao(parametro) # chama a classe e o método que faz a alteração do status.
        
        elif editar_valor is True: #realiza uma ação se caso o usuário queira alterar o valor, passando o editar_valor=True na chamada do método 
            self.consultar(parametro) # chama o método consultar da classe.
            alterar_dados.alterar_valor(parametro) # chama a classe e o método que faz a alteração do status.
        
        
        elif editar_quantidade is True: #realiza uma ação se caso o usuário queira alterar a quantidade, passando o editar_quantidade=True na chamada do método 
            self.consultar(parametro) # chama o método consultar da classe.
            alterar_dados.alterar_quantidade(parametro) # chama a classe e o método que faz a alteração do status.
        
        elif editar_status is True: #realiza uma ação se caso o usuário queira alterar o status do produto, passando o editar_status=True na chamada do método 
            self.consultar(parametro) # chama o método consultar da classe.
            alterar_dados.alterar_status(parametro) # chama a classe e o método que faz a alteração do status.

    


    def listar(self): # define o método listar
        with Session(engine) as session: # abre uma conexão no banco de dados
            pegar_todos_ativos = select(GestaoAtivos) # realiza uma consulta SQL na tabela Gestão ativos, e verifica se o paramentro é igual a variavel produto
            ativos_encontrados = session.exec(pegar_todos_ativos).all() # executa a consulta da linha anterior e pega todos os valores correspondentes

            return ativos_encontrados # retorna a consulta se ela for encontrada.





                








        




