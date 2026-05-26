# aiutati che dio t'aiuta 
import random


class Coin():
    
    def __init__(self, face = None):
        self.face = face

    def throw(self):
        result = random.randint(0,1)
        if result == 1:
            self.face = "Testa"
        else:
            self.face = "Croce"
        print(f'Il risultato del lancio: {self.face}')

# gigio = Coin()
# gigio.throw()

# ioboi

class Vehicle():

    def __init__(self, model, label, year, speed = 0):
        self.model = model
        self.label = label
        self.year = year
        self.speed = 0

    def __str__(self):
        print('Il veicolo è marcato {}, modello {} dell anno {}. La sua velocità è {}'.format(self.label, self.model, self.year, self.speed))
    
    def speed_up(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
    
    def get_speed(self):
        print(f'La velocità corrente è {self.speed}')
    

#gigio = Vehicle("Off Road", "Toy2", 2008, 24)
#gigio.__str__()
#gigio.speed_up()
#gigio.speed_up()
#gigio.brake()
#gigio.get_speed()

class CSVfile():

    