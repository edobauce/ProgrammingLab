import os

def conta_ogni(path):
    parole= {}
    try:
        with open(path,'r') as file:
            for parola in file.read().replace("\n", ",").split(","):
                if parola in parole:
                    parole[parola] +=1
                else:
                    parole[parola] = 1
            del parole[""]
        return parole             
    except FileNotFoundError:
        print("Errore nel path, impossibile procedere, programma concluso")
        main = False

def removedups(path):
    try:
        countr = 0
        with open("unique.txt", "w") as newfile:
            with open(path,'r') as file1:
                for parola1 in file1.read().split():
                    with open(path, "r") as file2:
                        for parola2 in file2.read().split():
                            if parola1 == parola2:
                                countr += 1
                        if countr == 1:
                            newfile.write(parola1)
                            countr = 0
    except FileNotFoundError:
        print("Errore nel path, impossibile procedere, programma concluso")
        main = False




main = True

while main:

    dict1 = {}
    filepath = input()
    print(removedups(filepath))