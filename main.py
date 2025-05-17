from entidades.criar_ativos import CriarAtivos # importa a classe CriarAtivos do módulo criar_ativos
import time # importa a biblioteca time para fazer uma pausa na execução do código
from funcoes_extras.funcao_clear import clear # importa a função clear, que limpa a tela do terminal
from decimal import Decimal, InvalidOperation # importa a classe Decimal e a exceção InvalidOperation da biblioteca decimal

class Menu(CriarAtivos): # define a classe Menu que herda da classe CriarAtivos
    
    def __init__(self): # define o método construtor da classe
        iniciar_programa = True # inicializa a variável iniciar_programa como True

        while iniciar_programa == True: # enquanto iniciar_programa for True
        
            print('''MENU INCIAL: 
            1 - Cadastrar
            2 - alterar
            3 - consultar
            4 - listar
            0 - sair''')# imprime o menu inicial
            print() # imprime uma linha em branco para pular uma linha na hora da exibição do menu
            
            escolher_opcao = int(input('Digite uma das opções acima: ')) # pede para o usuário escolher uma opção do menu

            if escolher_opcao == 1: # se o usuário escolher a opção 1
                clear() # limpa a tela do terminal
                self.exibir_tela_cadastro() # chama o método exibir_tela_cadastro da classe 
            
            elif escolher_opcao == 2: # se o usuário escolher a opção 2
                clear() # limpa a tela do terminal
                self.exibir_tela_alterar() # chama o método exibir_tela_alterar da classe
            
            elif escolher_opcao == 3: # se o usuário escolher a opção 3
                clear() # limpa a tela do terminal
                self.exibir_tela_consultar() # chama o método exibir_tela_consultar da classe
            
            elif escolher_opcao == 4: # se o usuário escolher a opção 4
                clear() # limpa a tela do terminal
                self.exibir_tela_listagem() # chama o método exibir_tela_listagem da classe
            
            elif escolher_opcao == 0: # se o usuário escolher a opção 0
                clear() # limpa a tela do terminal
                print('encerrando programa...') # imprime uma mensagem de encerramento
                time.sleep(1) # faz uma pausa de 1 segundo
                iniciar_programa = False # altera a variável iniciar_programa para False, encerrando o loop
            
            else: # se o usuário escolher uma opção inválida
                print('Opção inválida') # imprime uma mensagem de erro



    
    
    def exibir_tela_cadastro(self): # define o método exibir_tela_cadastro
        iniciar_loop = True # inicializa a variável iniciar_loop como True
        
        while iniciar_loop: # enquanto iniciar_loop for True
            print('Painel de cadastro: ') # imprime o título do painel de cadastro
            produto = input('Digite o nome do produto: ').title() # pede o nome do produto
            descricao = input('digite a descrição do produto: ') # pede a descrição do produto
            valor = input('Digite o valor do produto: ') # pede o valor do produto
            quantidade = input('Digite a quantidade do produto: ') # pede a quantidade do produto
            status = input('Digite o status do produto: (ativo/inativo) ').lower() # pede o status do produto, convertendo para minúsculas


            try: # tenta converter o valor e a quantidade para os tipos corretos
                valor = Decimal(valor) # converte o valor para Decimal
                quantidade = int(quantidade) # converte a quantidade para inteiro
                
            except InvalidOperation: # se ocorrer um erro de operação inválida ao converter o valor
                clear() # limpa a tela do terminal
                print(f'Campo "valor" inválido') # imprime uma mensagem de erro
                continue # volta o loop
            except ValueError: # se ocorrer um erro de valor ao converter a quantidade
                clear() # limpa a tela do terminal
                print(f'Campo "quantidade" inválido') # imprime uma mensagem de erro
                continue # volta o loop


            if status != 'ativo' and status != 'inativo': # se o status não for 'ativo' ou 'inativo'
                clear() # limpa a tela do terminal
                print('campo "status" inválido') # imprime uma mensagem de erro
                continue # volta o loop

            super().cadastrar(produto=produto, descricao=descricao, valor=valor, quantidade=quantidade, status=status) # chama o método cadastrar da classe CriarAtivos, passando os parâmetros do cadastro
            clear() # limpa a tela do terminal
            print('Cadastro realizado com sucesso.') # imprime uma mensagem de sucesso
            cadastrar_novamente = input('deseja realizar outro cadastro? (s/n) ').lower() # pergunta se o usuário deseja realizar outro cadastro
 
            if cadastrar_novamente == 's': # se o usuário escolher 's'
                clear() # limpa a tela do terminal
            else: # se o usuário escolher 'n'
                iniciar_loop = False # altera a variável iniciar_loop para False, encerrando o loop
                clear() # limpa a tela do terminal
                print('voltando ao menu inicial...') # imprime uma mensagem de retorno ao menu inicial
                time.sleep(1) # faz uma pausa de 1 segundo
                clear() # limpa a tela do terminal



    
    
    def exibir_tela_alterar(self): # define o método exibir_tela_alterar 
        iniciar_loop = True # inicializa a variável iniciar_loop como True

        while iniciar_loop: # enquanto iniciar_loop for True
        
            print('''O que deseja alterar: 
                1- alterar nome do produto.
                2- alterar a descrição do produto.
                3- alterar o valor do produto.
                4- alterar a quantidade do produto.
                5- alterar o status do produto.
                0- voltar ao menu inicial.''')# imprime o título do painel de alteração
            
            print()# imprime uma linha em branco para pular uma linha na hora da exibição do menu
            escolher_opcao = int(input('Escolha uma das opções: ')) # pede para o usuário escolher uma opção do menu
            clear() # limpa a tela do terminal

            if escolher_opcao == 0: # se o usuário escolher a opção 0
                clear() # limpa a tela do terminal
                print('Voltando para o menu inicial...') # imprime uma mensagem de retorno ao menu inicial
                time.sleep(1) # faz uma pausa de 1 segundo
                clear() # limpa a tela do terminal
                break # encerra o loop

            consultar_pelo_produto = input('Digite o nome do produto que deseja fazer a alteração: ').title() # pede o nome do produto a ser alterado
            consulta = super().consultar(consultar_pelo_produto) # chama o método consultar da classe CriarAtivos, passando o nome do produto a ser alterado

            if consulta: # se a consulta retornar um resultado
                print(f'''N° da Nota Fiscal: {consulta.nota_fiscal}    
                        ID: {consulta.id}
                        Produto: {consulta.produto}
                        Descrição: {consulta.descricao}
                        Valor: R$ {consulta.valor}
                        Quantidade: {consulta.quantidade}
                        Status: {consulta.status}''') # imprime os dados do produto encontrado
            else: # se a consulta não retornar resultado
                print('Produto não encontrado.')  # imprime uma mensagem dizendo que o produto não foi encontrado


            if escolher_opcao == 1: # se o usuário escolher a opção 1
                super().alterar(consultar_pelo_produto, editar_produto=True) # chama o método alterar da classe CriarAtivos, passando o nome do produto a ser alterado e o parâmetro editar_produto como True      
            elif escolher_opcao == 2: # se o usuário escolher a opção 2
                super().alterar(consultar_pelo_produto, editar_descricao=True) # chama o método alterar da classe CriarAtivos, passando o nome do produto a ser alterado e o parâmetro editar_descricao como True
            elif escolher_opcao == 3: # se o usuário escolher a opção 3
                super().alterar(consultar_pelo_produto, editar_valor=True) # chama o método alterar da classe CriarAtivos, passando o nome do produto a ser alterado e o parâmetro editar_valor como True
            elif escolher_opcao == 4: # se o usuário escolher a opção 4
                super().alterar(consultar_pelo_produto, editar_quantidade=True) # chama o método alterar da classe CriarAtivos, passando o nome do produto a ser alterado e o parâmetro editar_quantidade como True
            elif escolher_opcao == 5: # se o usuário escolher a opção 5
                super().alterar(consultar_pelo_produto, editar_status=True) # chama o método alterar da classe CriarAtivos, passando o nome do produto a ser alterado e o parâmetro editar_status como True
           

            opcao_continuar = input('Deseja Fazer mais alguma alteração? (s/n) ').lower() # pergunta se o usuário deseja fazer mais alguma alteração

            if opcao_continuar == 's': # se o usuário escolher 's'
                clear() # limpa a tela do terminal
            else: # se o usuário escolher 'n'
                iniciar_loop = False # altera a variável iniciar_loop para False, encerrando o loop
                clear() # limpa a tela do terminal
                print('Voltando para o menu...') # imprime uma mensagem de retorno ao menu
                time.sleep(1) # faz uma pausa de 1 segundo
                clear() # limpa a tela do terminal

             
                    

    
    
    def exibir_tela_consultar(self): # define o método exibir_tela_consultar
        iniciar_loop = True # inicializa a variável iniciar_loop como True


        while  iniciar_loop: # enquanto iniciar_loop for True
        
            buscar_pelo_produto = input('Digite o nome do produto que deseja consultar: ').title() # pede o nome do produto a ser consultado
            consulta = super().consultar(buscar_pelo_produto) # chama o método consultar da classe CriarAtivos, passando o nome do produto a ser consultado

            if consulta: # se a consulta retornar um resultado
                print(f'''N° da Nota Fiscal: {consulta.nota_fiscal}   
                        ID: {consulta.id}
                        Produto: {consulta.produto}
                        Descrição: {consulta.descricao}
                        Valor: R$ {consulta.valor}
                        Quantidade: {consulta.quantidade}
                        Status: {consulta.status}''') # imprime os dados do produto encontrado
                
                condicao = input('Deseja realizar outra consulta? (s/n) ').lower() # pergunta se o usuário deseja realizar outra consulta

                if condicao == 's': # se o usuário escolher 's'
                    clear() # limpa a tela do terminal
                else: # se o usuário escolher 'n'
                    iniciar_loop = False # altera a variável iniciar_loop para False, encerrando o loop
                    clear() # limpa a tela do terminal
                    print('Voltando ao menu inicial...') # imprime uma mensagem de retorno ao menu inicial
                    time.sleep(1) # faz uma pausa de 1 segundo
                    clear() # limpa a tela do terminal
            else: # se a consulta não retornar resultado
                print('produto não encontrado.') # imprime uma mensagem dizendo que o produto não foi encontrado
                tentar_novamente = input('deseja tentar consultar novamente? (s/n)').lower() # pergunta se o usuário deseja tentar consultar novamente
                if tentar_novamente == 's': # se o usuário escolher 's'
                    clear() # limpa a tela do terminal
                else: # se o usuário escolher 'n'
                    iniciar_loop = False # altera a variável iniciar_loop para False, encerrando o loop
                    clear() # limpa a tela do terminal
                    print('Voltando ao menu inicial...') # imprime uma mensagem de retorno ao menu inicial
                    time.sleep(1) # faz uma pausa de 1 segundo
                    clear() # limpa a tela do terminal
    
    
    
    
    
    def exibir_tela_listagem(self): # define o método exibir_tela_listagem
        lista_de_ativos = super().listar() # chama o método listar da classe CriarAtivos, que retorna uma lista de ativos cadastrados
        
        if lista_de_ativos: # se a lista de ativos não estiver vazia
            print('***************RELATÓRIO***************') # imprime o título do relatório
            print() # imprime uma linha em branco para pular uma linha na hora da exibição do relatório
            for ativo in lista_de_ativos: # para cada ativo na lista de ativos
                print(20 * '-') # imprime uma linha de separação
                print(f'''N° da Nota Fiscal: {ativo.nota_fiscal}    
                        ID: {ativo.id}
                        Produto: {ativo.produto}
                        Descrição: {ativo.descricao}
                        Valor: R$ {ativo.valor}
                        Quantidade: {ativo.quantidade}
                        Status: {ativo.status}''') # imprime os dados do ativo
                print(20 * '-') # imprime outra linha de separação
            input('Aperte qualquer tecla para voltar ao menu inicial.') # pede para o usuário apertar qualquer tecla para voltar ao menu inicial
            clear() # limpa a tela do terminal
            print('Voltando ao menu inicial...') # imprime uma mensagem de retorno ao menu inicial
            time.sleep(1) # faz uma pausa de 1 segundo
            clear() # limpa a tela do terminal
        else:
            print('Nenhum Ativo Encontrado.') # imprime uma mensagem dizendo que nenhum ativo foi encontrado
            input('aperte a tecla enter para voltar ao menu inicial') # pede para o usuário apertar a tecla enter para voltar ao menu inicial
            clear() # limpa a tela do terminal
            print('voltando ao menu inicial...') # imprime uma mensagem de retorno ao menu inicial
            clear() # limpa a tela do terminal






r = Menu()
