from randomitems import randomitem
import random

# Classe canguro con __init con contenuto_tasca come lista con def param = lista vuota
# metodo intasca che inserisce un oggetto nella tasca
# un metodo __str che restituisce una rappresentazione di canguro e degli oggetti nella sua tasca

class Canguro():
    
    def __init__(self, nome):
        self.contenuto_tasca = []
        self.nome = nome

    def intasca(self, object):
        self.contenuto_tasca.append(object)
    
    def __str__(self):
        return 'Il Canguro {} ha rubato {}'.format(self.nome, self.contenuto_tasca)
    
gigi = Canguro("Gigi")
bagigi = Canguro("Bagigi")

for i in range(random.randint(1,20)):
    gigi.intasca(randomitem())

for i in range(random.randint(1,20)):
    bagigi.intasca(randomitem())

print(gigi)
print(bagigi)