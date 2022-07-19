# Criando a classe Banco

class Banco:
    
    # Método construtor com um atributo privado e outro público.
    
    def __init__(self, saldo, nome):
        self.__saldo = saldo
        self.nome = nome

    
    # @property faz com que a acesse os métodos agora por funções
    
    @property
    def saldo(self):
        return self.__saldo

    
    # @saldo.setter faz agora com que a gente atualize valores privados.
    
    @saldo.setter
    def saldo(self, price):
        return self.__saldo == price


objeto = Banco(500, 'Carlos')

money = objeto.saldo = 200

print(money)