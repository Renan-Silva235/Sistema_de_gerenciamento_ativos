from banco_de_dados.base_dados import GestaoAtivos, engine # importa o módulo do banco de dados
from sqlmodel import Session, select # importa a biblioteca sqlmodel e suas classes e métodos

def gerar_nota_fiscal(): # define a função que gera o cpf
    with Session(engine) as session: # abre uma conexão no banco de dados
        resultado = session.exec(select(GestaoAtivos)).all() # # realiza uma consulta SQL na tabela GestaoAtivos e executa.
        numero_da_nota = len(resultado) + 1 #pega o tamanho dos registros e soma + 1 para não ter número de nota repetida.
        return f'{numero_da_nota:09}' # retorna o número da nota adicionando 8 zeros a esquerda.