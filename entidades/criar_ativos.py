from sqlmodel import Session, select  # importa a biblioteca sqlmodel e seus métodos e classes
from banco_de_dados.base_dados import GestaoAtivos, engine # importa o módulo onde está o código do banco de dados, e o banco de dados
from decimal import Decimal # importa a biblioteca decimal, para números com casas decimais
from nota_fiscal.gerar_nota_fiscal import gerar_nota_fiscal # importa a função de gerar a nota fiscal
from funcoes_de_alteracao.alterar_status import alterar_status # importa a função que altera o status

class CriarAtivos:  # Cria uma classe que contém as funcionalidades do sistema
    

    
    def cadastrar(self, produto, descricao, valor, quantidade, status): # define o método para cadastro.
       
        with Session(engine) as session: # abre uma conexão no banco de dados.

            # configura os dados para serem salvos no banco de dados
            registrar_dados = GestaoAtivos(nota_fiscal=gerar_nota_fiscal(), produto=produto.title(), descricao=descricao, valor=valor.quantize(Decimal('0.01')), quantidade=quantidade, status=status)
            session.add(registrar_dados) # prepara os dados para serem salvos no banco de dados
            session.commit() # envia os dados para o banco de dados
      


    def consultar(self, produto):  # define o método consultar
           
        with Session(engine) as session: # abre uma conhexão no banco de dados
            produto_consultado = select(GestaoAtivos).where(GestaoAtivos.produto == produto) # realiza uma consulta SQL na tabela Gestão ativos, e verifica se o paramentro é igual a variavel produto
            produto_consultado = session.exec(produto_consultado).first() # executa a consulta da linha anterior e pega o primeiro valor correspondente 
            
            if produto_consultado: # se o produto for encontrado
                print(f'''N° da Nota Fiscal: {produto_consultado.nota_fiscal}   
                    Produto: {produto_consultado.produto}
                    Descrição: {produto_consultado.descricao}
                    Valor: R$ {produto_consultado.valor}
                    Quantidade: {produto_consultado.quantidade}
                    Status: {produto_consultado.status}''')  #realiza um print exibindo todos os dados do produto consultado
            else:
                print('Produto não encontrado') # exibe uma mensagem se o produto consultado não for encontrado.

    
    
    def alterar(self, parametro, editar_produto=False, editar_descricao=False, editar_status=False): # define o método alterar
        
        if editar_status is True: #realiza uma ação se caso o usuário queira alterar o status do produto, passamdo o editar_status=True na chamada do método 
            self.consultar(parametro) # chama o método consultar da classe.
            alterar_status(parametro) # chama a função que faz a alteração do status.

    


    def listar(self): # define o método listar
        pass



                








        




