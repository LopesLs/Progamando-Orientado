'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

class Fibonnaci:

    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.iteravel = 3
        self.valor1 = 0
        self.valor2 = 1

    def calcula_sequencia(self):
        print(f'{self.valor1} --> {self.valor2}', end = '')

        while self.iteravel <= self.quantidade:
            self.novo_valor = self.valor1 + self.valor2
            print(f' --> {self.novo_valor}', end = '')
            self.valor1 = self.valor2
            self.valor2 = self.novo_valor
            self.iteravel += 1
        
        return '\nAcabou'

if __name__ == '__main__':
    obj = Fibonnaci(7)
    print(obj.calcula_sequencia())