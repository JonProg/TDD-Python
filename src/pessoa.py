import requests

class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obitidos = False
    
    def obter_todos_os_dados(self):
        resposta = requests.get('')

        if resposta.ok:
            self.dados_obitidos = True
            return 'CONECTADO'
        else:
            self.dados_obitidos = False
            return 'ERRO 404'