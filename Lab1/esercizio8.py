class Veicolo():

    def __init__(self, marca, modello, anno, veicolo):
        default_speed = 0
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = default_speed
        self.veicolo = veicolo

    def __str__(self):
            return f"Veicolo: Marca {self.marca} - Modello {self.modello} - Anno {self.anno} - Speed {self.speed}"
        
    def accelerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5

    def get_speed(self):
        print(f"La velocità è: {self.speed}")
    
    def start(self):
        for i in range(13):
            self.accelerare()
            if self.speed >= 50:
                self.frenare()

class Auto(Veicolo):

    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno, "Auto")
        self.numero_porte = numero_porte

    def __str__(self):
        return f"Tipologia veicolo: {self.veicolo}. Marca: {self.marca}. Modello: {self.modello}. Numero di porte: {self.numero_porte}. Anno: {self.anno}."
        

class Moto(Veicolo):

    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno, "Moto")
        self.tipo = tipo

    def __str__(self):
        return f"Tipologia veicolo: {self.veicolo}. Marca: {self.marca}. Modello: {self.modello}. Assetto: {self.tipo}. Anno: {self.anno}."
        
    

car = Auto("Volkswagen", "Polo", "2018", 5)
bike = Moto("BMW", "E4", "2021", "Sportivo")


print(car)
print(bike)

car.start()
car.get_speed()

bike.start()
bike.frenare()
bike.frenare()
bike.get_speed()


