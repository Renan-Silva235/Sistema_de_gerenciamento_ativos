from sqlmodel import Session, select # importa a biblioteca sqlmodel e seus métodos e classes
from banco_de_dados.base_dados import GestaoAtivos, engine # importa o módulo onde está o código do banco de dados, e o banco de dados
from decimal import Decimal # importa a biblioteca decimal, para números com casas decimais
from funcoes_extras.funcao_clear import clear # importa a função clear, que limpa a tela do terminal
import time # importa a biblioteca time, para fazer uma pausa na execução do código


class AlterarDados: # define a classe que contém as funcionalidades de alteração de dados

    def alterar_nome_produto(self, produto): # define o método para alterar o nome do produto
         with Session(engine) as session: # abre uma conexão no banco de dados
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto) # realiza uma consulta SQL na tabela Gestão ativos, e verifica se o paramentro é igual a variavel produto
            produto_encontrado = session.exec(buscar_produto).first() # executa a consulta da linha anterior e pega o primeiro valor correspondente

            if produto_encontrado:# verifica se o produto foi encontrado
                opcao_de_alteracao = input('Realmente deseja alterar o nome do Produto? (s/n) ').lower() # pergunta se o usuário realmente deseja alterar o nome do produto

                if opcao_de_alteracao == 's': # verifica se o usuário digitou 's' para sim
                    novo_nome = input('Digite o novo nome para o produto: ').title() # pede o novo nome do produto
                    produto_encontrado.produto = novo_nome # altera o nome do produto no banco de dados
                    clear() # limpa a tela do terminal
                    print('nome atualizado com sucesso') # imprime uma mensagem de sucesso
                    time.sleep(1) # faz uma pausa de 1 segundo
                    session.add(produto_encontrado) # adiciona o produto alterado na sessão
                    session.commit() # salva as alterações no banco de dados
                else: # se o usuário não quiser alterar o nome do produto
                    clear() # limpa a tela do terminal
                 
                



    def alterar_descricao(self, produto): # define o método para alterar a descrição do produto
         with Session(engine) as session: # abre uma conexão no banco de dados
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto) # realiza uma consulta SQL na tabela Gestão ativos, e verifica se o paramentro é igual a variavel produto
            produto_encontrado = session.exec(buscar_produto).first() # executa a consulta da linha anterior e pega o primeiro valor correspondente

            if produto_encontrado:# verifica se o produto foi encontrado
                opcao_de_alteracao = input('Realmente deseja alterar a descrição do Produto? (s/n) ').lower() # pergunta se o usuário realmente deseja alterar a descrição do produto

                if opcao_de_alteracao == 's': # verifica se o usuário digitou 's' para sim
                    nova_descricao = input('Digite uma nova descrição para o produto: ').title() # pede a nova descrição do produto
                    produto_encontrado.descricao = nova_descricao # altera a descrição do produto no banco de dados
                    clear() # limpa a tela do terminal
                    print('descrição atualizada com sucesso') # imprime uma mensagem de sucesso
                    time.sleep(1) # faz uma pausa de 1 segundo
                    session.add(produto_encontrado) # adiciona o produto alterado na sessão
                    session.commit() # salva as alterações no banco de dados
                else: # se o usuário não quiser alterar a descrição do produto
                    clear() # limpa a tela do terminal
                   
                    


    def alterar_valor(self, produto): # define o método para alterar o valor do produto
         with Session(engine) as session: # abre uma conexão no banco de dados
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto) # realiza uma consulta SQL na tabela Gestão ativos, e verifica se o paramentro é igual a variavel produto
            produto_encontrado = session.exec(buscar_produto).first() # executa a consulta da linha anterior e pega o primeiro valor correspondente
 
            if produto_encontrado: # verifica se o produto foi encontrado
                opcao_de_alteracao = input('Realmente deseja alterar o valor do Produto? (s/n) ').lower() # pergunta se o usuário realmente deseja alterar o valor do produto

                if opcao_de_alteracao == 's': # verifica se o usuário digitou 's' para sim
                    novo_valor = Decimal(input('Digite o novo valor para o produto: ')) # pede o novo valor do produto
                    produto_encontrado.valor = novo_valor # altera o valor do produto no banco de dados                    
                    clear() # limpa a tela do terminal
                    print('valor atualizado com sucesso') # imprime uma mensagem de sucesso
                    time.sleep(1) # faz uma pausa de 1 segundo
                    session.add(produto_encontrado)  # adiciona o produto alterado na sessão
                    session.commit() # salva as alterações no banco de dados
                else: # se o usuário não quiser alterar o valor do produto
                    clear() #   limpa a tela do terminal
                 
                   


    
    def alterar_quantidade(self, produto): # define o método para alterar a quantidade do produto
         with Session(engine) as session: # abre uma conexão no banco de dados
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto) # realiza uma consulta SQL na tabela Gestão ativos, e verifica se o paramentro é igual a variavel produto
            produto_encontrado = session.exec(buscar_produto).first() # executa a consulta da linha anterior e pega o primeiro valor correspondente

            if produto_encontrado: # verifica se o produto foi encontrado
                opcao_de_alteracao = input('Realmente deseja alterar a quantidade do Produto? (s/n) ').lower() # pergunta se o usuário realmente deseja alterar a quantidade do produto
 
                if opcao_de_alteracao == 's': # verifica se o usuário digitou 's' para sim
                    nova_quantidade = int(input('Digite a nova quantidade do produto: ')) # pede a nova quantidade do produto
                    produto_encontrado.quantidade = nova_quantidade # altera a quantidade do produto no banco de dados                    
                    clear() # limpa a tela do terminal
                    print('Quantidade atualizada com sucesso') # imprime uma mensagem de sucesso
                    time.sleep(1) # faz uma pausa de 1 segundo
                    session.add(produto_encontrado) # adiciona o produto alterado na sessão
                    session.commit() # salva as alterações no banco de dados
                else: # se o usuário não quiser alterar a quantidade do produto
                    clear() # limpa a tela do terminal
                
                 


    def alterar_status(self, produto): #    define o método para alterar o status do produto
    
        with Session(engine) as session: # abre uma conexão no banco de dados
            buscar_produto = select(GestaoAtivos).where(GestaoAtivos.produto == produto) # realiza uma consulta SQL na tabela Gestão ativos, e verifica se o paramentro é igual a variavel produto
            produto_encontrado = session.exec(buscar_produto).first() # executa a consulta da linha anterior e pega o primeiro valor correspondente
 
            if produto_encontrado: # verifica se o produto foi encontrado
                opcao_de_alteracao = input('Realmente deseja alterar o status do Produto? (s/n) ').lower() # pergunta se o usuário realmente deseja alterar o status do produto

                if opcao_de_alteracao == 's': # verifica se o usuário digitou 's' para sim
                    produto_encontrado.status ='inativo' if produto_encontrado.status == 'ativo' else 'ativo' # altera o status do produto no banco de dados
                    
                    clear() # limpa a tela do terminal
                    print('status atualizado com sucesso') # imprime uma mensagem de sucesso
                    time.sleep(1) # faz uma pausa de 1 segundo
                    session.add(produto_encontrado)  # adiciona o produto alterado na sessão
                    session.commit() # salva as alterações no banco de dados
                else: # se o usuário não quiser alterar o status do produto
                    clear() # limpa a tela do terminal
                 
                    
                 