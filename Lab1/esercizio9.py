class Poligono():

    def __init__(self, lati):
        self.lati = lati

    def __str__(self):
        return "Il poligono ha {} lati".format(self.lati)
    
class Quadrilatero(Poligono):

    def __init__(self, lati = 4):
        super().__init__(lati)

    def __str__(self):
        return "Sono un quadrilatero"
    
class Rettangolo(Quadrilatero):

    def __init__(self, base, altezza, lati = 4):
        super().__init__(lati)
        self.base = base
        self.altezza = altezza

    def perimetro_calc(self):
        perimetro = self.base * 2 + self.altezza * 2
        return perimetro
    
    def area_calc(self):
        area = self.base * self.altezza
        return area

    def __str__(self):
        return "Sono un quadrilatero di base {} e altezza {}, la mia area è {} e il mio perimetro è {}".format(self.base, self.altezza, self.area_calc(), self.perimetro_calc())
    
class Triangolo(Poligono):

    def __init__(self, lato1, lato2, lato3, lati = 3):
        super().__init__(lati)
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

    def perimetro_calc(self):
        perimetro = self.lato1 + self.lato2 + self.lato3
        return perimetro

    def is_equilatero(self):
        if self.lato1 == self.lato2 and self.lato1 == self.lato3:
            return True
        
    def __str__(self):
        if self.is_equilatero() == True:
            return "Sono un triangolo equilatero con lati {}, {} e {} e perimetro {}".format(self.lato1, self.lato2, self.lato3, self.perimetro_calc())
        else:
            return "Sono un triangolo non equilatero con lati {}, {} e {} e perimetro {}".format(self.lato1, self.lato2, self.lato3, self.perimetro_calc())
        

polix = Poligono(45)

print(polix)

quadratix = Quadrilatero()

print(quadratix)

rettangolix = Rettangolo(20, 30)

print(rettangolix)

triangolix = Triangolo(2, 3, 4)

print(triangolix)

triangolixmeglio = Triangolo(2, 2, 2)

print(triangolixmeglio)