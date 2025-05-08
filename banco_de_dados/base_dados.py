from sqlmodel import SQLModel, Field, create_engine # importa a biblioteca sqlmodel e suas classes e métodos
from decimal import Decimal # importa a biblioteca decimal, para números com casas decimais

class GestaoAtivos(SQLModel, table=True): # cria uma classe chamada GestaoAtivos que será o nome da tabela no banco de dados
    id: int = Field(primary_key=True) # cria um id para o usuário
    nota_fiscal: str = Field(max_length=9) # Cria a coluna nota_fiscal 
    produto: str = Field(max_length=100) # cria a coluna produto
    descricao: str = Field(max_length=100) # cria a coluna descricao
    valor: Decimal = Field(default=0, decimal_places=2) # cria a coluna valor
    quantidade: int # cria a coluna quantidade
    status: str = Field(max_length=15) # cria a coluna status

arquivo_sqlite = 'banco_de_dados/db_gestao_ativo.db' # Nome e caminho do arquivo SQLite onde os dados serão armazenados.
conectar_string = f'sqlite:///{arquivo_sqlite}' # String de conexão com o banco usando o SQLite.
engine = create_engine(conectar_string, echo=False) # gerencia a conexão no banco de dados.


if __name__ == '__main__': # garante que o banco seja criado apenas se o arquivo base_dados.py é executado, e se não existir
    SQLModel.metadata.create_all(engine) # cria o banco de dados.





