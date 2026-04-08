"""

class Veicolo:

    def __init__(self, modello, marca, anno, speed):
        
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

        def __str__(self):
            
            return f"Veicolo: Marca {self.marca} - Modello {self.modello} - Anno {self.anno} - Speed {self.speed}"
        
        def accelerare(self):
            self.speed += 5

        def frenare(self):
            self.speed -= 5

        def get_speed(self):
            return self.get_speed
    
def start():
    for i in range(10):
        car.accelera()
        car.

car = Veicolo("Polo", "Volkswagen", 2018, 0)

"""

class CSVFile:
    
    def __init__(self, name_file):
        self.name_file = name_file
    
    def get_data(self):
        with open(self.name_file, "r") as file:
            list = []
            for rows in file:
                rows = rows.strip().split(",") # rimuove \n e divide gli elementi separati dalla virgola
                list.extend(x for x in rows if x)
                return list
            
file = CSVFile(input())
print
