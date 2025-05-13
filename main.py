from entidades.criar_ativos import CriarAtivos
import time
from funcoes_extras.funcao_clear import clear
from decimal import Decimal, InvalidOperation

class Menu(CriarAtivos):
    
    def __init__(self):
        iniciar_programa = True

        while iniciar_programa == True:
        
            print('''MENU INCIAL:
            1 - Cadastrar
            2 - alterar
            3 - consultar
            4 - listar
            0 - sair''')
            print()
            
            escolher_opcao = int(input('Digite uma das opções acima: '))

            if escolher_opcao == 1:
                clear()
                self.exibir_tela_cadastro()
            
            elif escolher_opcao == 2:
                clear()
                self.exibir_tela_alterar()
            
            elif escolher_opcao == 3:
                clear()
                self.exibir_tela_consultar()
            
            elif escolher_opcao == 4:
                clear()
                self.exibir_tela_listagem()
            
            elif escolher_opcao == 0:
                clear()
                print('encerrando programa...')
                time.sleep(2)
                iniciar_programa = False
            
            else:
                print('Opção inválida')



    
    
    def exibir_tela_cadastro(self):
        iniciar_loop = True
        
        while iniciar_loop:
            print('Painel de cadastro: ')
            produto = input('Digite o nome do produto: ').title()
            descricao = input('digite a descrição do produto: ')
            valor = input('Digite o valor do produto: ')
            quantidade = input('Digite a quantidade do produto: ')
            status = input('Digite o status do produto: (ativo/inativo) ').lower()


            try:
                valor = Decimal(valor)
                quantidade = int(quantidade)
                
            except InvalidOperation:
                clear()
                print(f'Campo "valor" inválido')
                continue
            except ValueError:
                clear()
                print(f'Campo "quantidade" inválido')
                continue


            if status != 'ativo' and status != 'inativo':
                clear()
                print('campo "status" inválido')
                continue

            super().cadastrar(produto=produto, descricao=descricao, valor=valor, quantidade=quantidade, status=status)
            clear()
            print('Cadastro realizado com sucesso.')
            cadastrar_novamente = input('deseja realizar outro cadastro? (s/n) ').lower()

            if cadastrar_novamente == 's':
                clear()
            else:
                iniciar_loop = False
                clear()
                print('voltando ao menu inicial...')
                time.sleep(2)
                clear()



    
    
    def exibir_tela_alterar(self):
        iniciar_loop = True

        while iniciar_loop:
        
            print('''O que deseja alterar: 
                1- alterar nome do produto.
                2- alterar a descrição do produto.
                3- alterar o valor do produto.
                4- alterar a quantidade do produto.
                5- alterar o status do produto.
                0- voltar ao menu inicial.''')
            
            print()
            escolher_opcao = int(input('Escolha uma das opções: '))
            clear()

            if escolher_opcao == 0:
                clear()
                print('Voltando para o menu inicial...')
                time.sleep(2)
                clear()
                break

            consultar_pelo_produto = input('Digite o nome do produto que deseja fazer a alteração: ').title()
            consulta = super().consultar(consultar_pelo_produto)

            if consulta:
                print(f'''N° da Nota Fiscal: {consulta.nota_fiscal}   
                        ID: {consulta.id}
                        Produto: {consulta.produto}
                        Descrição: {consulta.descricao}
                        Valor: R$ {consulta.valor}
                        Quantidade: {consulta.quantidade}
                        Status: {consulta.status}''')
            else:
                print('Produto não encontrado.') 


            if escolher_opcao == 1:
                super().alterar(consultar_pelo_produto, editar_produto=True)        
            elif escolher_opcao == 2:
                super().alterar(consultar_pelo_produto, editar_descricao=True)
            elif escolher_opcao == 3:
                super().alterar(consultar_pelo_produto, editar_valor=True)
            elif escolher_opcao == 4:
                super().alterar(consultar_pelo_produto, editar_quantidade=True)
            elif escolher_opcao == 5:
                super().alterar(consultar_pelo_produto, editar_status=True)
           

            opcao_continuar = input('Deseja Fazer mais alguma alteração? (s/n) ').lower()

            if opcao_continuar == 's':
                clear()
            else:
                iniciar_loop = False
                clear()
                print('Voltando para o menu...')
                time.sleep(2)
                clear()

             
                    

    
    
    def exibir_tela_consultar(self):
        iniciar_loop = True


        while  iniciar_loop:
        
            buscar_pelo_produto = input('Digite o nome do produto que deseja consultar: ').title()
            consulta = super().consultar(buscar_pelo_produto)

            if consulta:
                print(f'''N° da Nota Fiscal: {consulta.nota_fiscal}   
                        ID: {consulta.id}
                        Produto: {consulta.produto}
                        Descrição: {consulta.descricao}
                        Valor: R$ {consulta.valor}
                        Quantidade: {consulta.quantidade}
                        Status: {consulta.status}''') 
                
                condicao = input('Deseja realizar outra consulta? (s/n) ').lower()

                if condicao == 's':
                    clear()
                else:
                    iniciar_loop = False
                    clear()
                    print('Voltando ao menu inicial...')
                    time.sleep(2)
                    clear()
            else:
                print('produto não encontrado.')
                tentar_novamente = input('deseja tentar consultar novamente? (s/n)').lower()
                if tentar_novamente == 's':
                    clear()
                else:
                    iniciar_loop = False
                    clear()
                    print('Voltando ao menu inicial...')
                    time.sleep(2)
                    clear()
    
    
    
    
    
    def exibir_tela_listagem(self):
        lista_de_ativos = super().listar()
        
        if lista_de_ativos:
            print('***************RELATÓRIO***************')
            print()
            for ativo in lista_de_ativos:
                print(20 * '-')
                print(f'''N° da Nota Fiscal: {ativo.nota_fiscal}   
                        ID: {ativo.id}
                        Produto: {ativo.produto}
                        Descrição: {ativo.descricao}
                        Valor: R$ {ativo.valor}
                        Quantidade: {ativo.quantidade}
                        Status: {ativo.status}''') 
                print(20 * '-')
            input('Aperte qualquer tecla para voltar ao menu inicial.')
            clear()
            print('Voltando ao menu inicial...')
            time.sleep(2)
            clear()
        else:
            print('Nenhum Ativo Encontrado.')
            input('aperte a tecla enter para voltar ao menu inicial')
            clear()
            print('voltando ao menu inicial...')
            clear()






r = Menu()
