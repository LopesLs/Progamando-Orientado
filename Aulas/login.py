# Criar uma classe com os atributos de login e senha.

class Conta:

    def __init__(self, nome : str = None, login : str = None, senha : str = None):
       self.nome = nome
       self.login = login
       self.senha = senha
    
    def verifica(self):
        
        if type(self.nome) != str or type(self.senha) != str:
            return 'Informe-nos um texto para efetuar o login'
        
        elif self.nome != self.nome.upper():
            return 'Informe o self.nome apenas em caixa baixa'
        
        elif self.login != self.login.lower():
            return 'Informe apenas em caixa baixa'

if __name__ == '__main__':
    instancia = Conta(login = 12234)