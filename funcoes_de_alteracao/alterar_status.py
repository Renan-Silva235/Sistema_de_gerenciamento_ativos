from sqlmodel import Session, select
from banco_de_dados.base_dados import GestaoAtivos, engine
import os
import time

def alterar_status(produto):
    
    with Session(engine) as session:
        buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto)
        produto_encontrado = session.exec(buscar_produto).first()

        if produto_encontrado:
            opcao_de_alteracao = input('Deseja alterar o status do Produto? (s/n) ').lower()

            if opcao_de_alteracao == 's':
                produto_encontrado.status ='inativo' if produto_encontrado.status == 'ativo' else 'ativo'
                
                os.system('clear')
                print('status atualizado com sucesso')
                time.sleep(2)
                session.add(produto_encontrado)
                session.commit()
            else:
                os.system('clear')
                print('Voltando para o menu...')
                time.sleep(2)
                return False

