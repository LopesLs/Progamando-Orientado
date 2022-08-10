class Corpos_Celestes():
    def __init__(self, nome_corpo_celeste, massa, luminosidade, diametro, tipo):
        self.massa = massa
        self.luminosidade = luminosidade
        self.diametro = diametro
        self.nome = nome_corpo_celeste
        self.tipo = tipo
    def __str__(self):
        return f''

class Planetas(Corpos_Celestes):
    def __init__(self, nome_planeta, massa, luminosidade, diametro, tipo, estrela_orbitada, anel : bool):
        super().__init__(nome_planeta, massa, luminosidade, diametro,tipo)
        self.estrela = estrela_orbitada
        self.anel = anel
       

class Estrela(Corpos_Celestes):
    def __init__(self, nome_estrela, massa, luminosidade, diametro, tipo, distancia):
        super().__init__(nome_estrela, massa, luminosidade, diametro,tipo)
        self.distancia = distancia
    def paralaxe(self, anguloparalaptico):
        pass

