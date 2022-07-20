class Fatorial:

    def __init__(self, number):
        self.number = number
        self.fatorial = 1
    
    def calculo_fatorial(self):
        for y in range(self.number, 0, -1):
            self.fatorial = self.fatorial * y
        
        return self.fatorial

if __name__ == '__main__':
    object = Fatorial(5)
    print(object.calculo_fatorial())