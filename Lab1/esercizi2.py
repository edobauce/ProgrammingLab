import os


def csvintolistsplitter(path):
    list1 = []
    try:
        with open(path, "r") as file1:
            for line in file1: # per ogni linea nel file
                elements = line.strip().split(",") # rimuove \n e divide gli elementi separati dalla virgola
                list1.extend(x for x in elements if x) # rimuove l'accapo vuoto, aggiungendo SEPARATAMENTE ( extend e non append ) ogni elemento se non è appunto l'accapo vuoto
        return(list1)
    except FileNotFoundError:
        print("Errore nel path, impossibile procedere, programma concluso")
        main = False

def txtintolistsplitter(path):
    list1 = []
    try:
        with open(path, "r") as file1:
            for line in file1: # per ogni linea nel file
                elements = line.strip().split(" ") # rimuove \n e divide gli elementi separati dallo spazio
                list1.extend(x for x in elements if x) # rimuove l'accapo vuoto, aggiungendo SEPARATAMENTE ( extend e non append ) ogni elemento se non è appunto l'accapo vuoto
        return(list1)
    except FileNotFoundError:
        print("Errore nel path, impossibile procedere, programma concluso")
        main = False

def listcomparerwinputelement(list1, inputelement):
    counter = 0
    for i in range(0, len(list1)):
        if list1[i] == inputelement:
            counter += 1
    return(counter)

main = True

while main:

    filepath = input()
    print("Il file è un file txt, csv o altro?")
    extensioninput = input()
    if extensioninput == "csv":
        listpippo = csvintolistsplitter(filepath)
    elif extensioninput == "txt":
        listpippo = txtintolistsplitter(filepath)
    else:
        print("Programma concluso")
        main = False
    print("Inserisci un elemento per ricercarlo nel file")
    inputelement = input()
    print(f"L'elemento {inputelement} è presente {listcomparerwinputelement(listpippo, inputelement)} volte")

    