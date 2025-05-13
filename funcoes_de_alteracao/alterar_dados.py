from sqlmodel import Session, select
from banco_de_dados.base_dados import GestaoAtivos, engine
from decimal import Decimal
from funcoes_extras.funcao_clear import clear
import time


class AlterarDados:

    def alterar_nome_produto(self, produto):
         with Session(engine) as session:
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto)
            produto_encontrado = session.exec(buscar_produto).first()

            if produto_encontrado:
                opcao_de_alteracao = input('Realmente deseja alterar o nome do Produto? (s/n) ').lower()

                if opcao_de_alteracao == 's':
                    novo_nome = input('Digite o novo nome para o produto: ').title()
                    produto_encontrado.produto = novo_nome                    
                    clear()
                    print('nome atualizado com sucesso')
                    time.sleep(2)
                    session.add(produto_encontrado)
                    session.commit()
                else:
                    clear()
                 
                



    
    
    
    
    def alterar_descricao(self, produto):
         with Session(engine) as session:
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto)
            produto_encontrado = session.exec(buscar_produto).first()

            if produto_encontrado:
                opcao_de_alteracao = input('Realmente deseja alterar a descrição do Produto? (s/n) ').lower()

                if opcao_de_alteracao == 's':
                    nova_descricao = input('Digite uma nova descrição para o produto: ').title()
                    produto_encontrado.descricao = nova_descricao                    
                    clear()
                    print('descrição atualizada com sucesso')
                    time.sleep(2)
                    session.add(produto_encontrado)
                    session.commit()
                else:
                    clear()
                   
                    


    
    
    
    
    def alterar_valor(self, produto):
         with Session(engine) as session:
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto)
            produto_encontrado = session.exec(buscar_produto).first()

            if produto_encontrado:
                opcao_de_alteracao = input('Realmente deseja alterar o valor do Produto? (s/n) ').lower()

                if opcao_de_alteracao == 's':
                    novo_valor = Decimal(input('Digite o novo valor para o produto: '))
                    produto_encontrado.valor = novo_valor                    
                    clear()
                    print('valor atualizado com sucesso')
                    time.sleep(2)
                    session.add(produto_encontrado)
                    session.commit()
                else:
                    clear()
                 
                   


    
    
    
    
    def alterar_quantidade(self, produto):
         with Session(engine) as session:
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto)
            produto_encontrado = session.exec(buscar_produto).first()

            if produto_encontrado:
                opcao_de_alteracao = input('Realmente deseja alterar a quantidade do Produto? (s/n) ').lower()

                if opcao_de_alteracao == 's':
                    nova_quantidade = int(input('Digite a nova quantidade do produto: '))
                    produto_encontrado.quantidade = nova_quantidade                    
                    clear()
                    print('Quantidade atualizada com sucesso')
                    time.sleep(2)
                    session.add(produto_encontrado)
                    session.commit()
                else:
                    clear()
                
                 


    
    
    
    def alterar_status(self, produto):
    
        with Session(engine) as session:
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto)
            produto_encontrado = session.exec(buscar_produto).first()

            if produto_encontrado:
                opcao_de_alteracao = input('Realmente deseja alterar o status do Produto? (s/n) ').lower()

                if opcao_de_alteracao == 's':
                    produto_encontrado.status ='inativo' if produto_encontrado.status == 'ativo' else 'ativo'
                    
                    clear()
                    print('status atualizado com sucesso')
                    time.sleep(2)
                    session.add(produto_encontrado)
                    session.commit()
                else:
                    clear()
                 
                    
                