import os # Importa o módulo os para interagir com o sistema operacional


def clear(): # Função para limpar a tela do terminal
    if os.name == 'nt': # Verifica se o sistema operacional é Windows
        os.system('cls')# Limpa a tela do terminal no Windows
    else: # Se não for Windows (Linux ou Mac)
        os.system('clear') # Limpa a tela do terminal no Linux ou Mac
