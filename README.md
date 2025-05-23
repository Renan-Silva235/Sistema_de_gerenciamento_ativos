Segue abaixo o passo a passo para a instalação dos pacotes, para funcionar a execução do software.

- Primeiramente, crie um ambiente virtual, no terminal execute o comando abaixo:

  python -m venv .env

- Depois ative o ambiente virtual com os seguintes comandos:

  Caso esteja usando o CMD, execute o comando abaixo:
  
    .env\Scripts\activate.bat

  Caso esteja usando o PowerShell, execute o comando abaixo:
    
  .env\Scripts\Activate.ps1


Depois que ativar o ambiente virtual, instale os pacotes e as suas dependências, no terminal execute o seguinte comando:

pip install requirements.txt

Se caso der erro, execute o comando abaixo:

pip install -r requirements.txt

pronto, Agora execute o programa com o comando abaixo:
    
    python -u main.py


- Caso queira visualizar a tabela no banco de dados, no VsCode instale a extensão SQLite Viewer
