"""
# Esercizio 1

# Stampare l'equivalente di 538 minuti nel formato h:min

def minute_converter(min):
    hours = int(min/60)
    minutes = min%60
    return(f"{hours}h:{minutes}min")

user_mininput = int(input("Inserisci un tempo in minuti da convertire: "))
print(minute_converter(user_mininput))

"""
"""

# Esercizio 2

# Una funzione che prende una parola e una lettera e ritorna quante volte quella lettera si ripete nella parola

def word_counter(word, letter):
    counter = 0
    word_lenght = 0
    for letters in word:
        if letter == word[word_lenght]:
            counter += 1
        word_lenght += 1
    return counter

user_wordinput = input("Inserisci una parola: ")
user_letterinput = input("\nInserisci una lettera: ")

print(f"\nNella parola {user_wordinput} ci sono {word_counter(user_wordinput, user_letterinput)} {user_letterinput}")

"""
"""

# Esercizio 3

# Scrivere una funzione che torna TRUE se la stringa inserita è palindroma (non ho voglia di finirlo)

def IsPal(Input_value):
    Pal = False
    lenght = len(Input_value)
    print(lenght)
    for i in range(lenght):
        if Input_value[i] != Input_value[lenght - i]:
            return Pal
    Pal = True

value = input("Inserisci una parola per verificare se è palindroma: ")
print(f"\nValore: {IsPal(value)}")

"""
"""

# Esercizio 5 

# Scrivere una funzione per fattorializzaare

def Facto(number):
    clang = 1
    for i in range(2, number+1):
        print(clang)
        clang = clang * i
    return clang

numbero = int(input())
risuldad = Facto(numbero)
print(risuldad)

"""

"""

# Esercizio 6

# Scrivere una funzione che prende in input due liste e ritorna TRUE se hanno almeno un elemento in comune

list_1 = []
list_2 = []

def user_generic_list_filler(list):
    flaglister = True
    print("Aggiungi un elemento alla lista: ")
    while flaglister:
        answ = input()
        if answ == "N" or answ == "No" or answ == "NO" or answ == "n" or answ == "no":
            flaglister = False
        else:    
            try:
                int(answ)
                print(f"Il numero {answ} è stato aggiunto alla lista, per concludere digitare N, per continuare inserire un altro elemento")
                list.append(answ)
            except ValueError:
                print(f"La stringa {answ} è stata aggiunta alla lista, per concludere digitare N, per continuare inserire un altro elemento")
                list.append(answ)
    return

def list_comparison(list1, list2):
    comparison = False
    while comparison == False:
        for i in range(0, len(list1)):
            for k in range(0, len(list2)):
                if list2[k] == list1[i]:
                    comparison = True
                    return comparison
        return comparison


user_list_filler(list_1)
user_list_filler(list_2)

print(list_1)
print(list_2)

print(f"Ci sono elementi in comune fra le due liste? {list_comparison(list_1, list_2)}")

"""

"""

# Esercizio 7

# Scrivere una funzione che presa in input una lista di numeri interi restituisca una lista composta di numeri come stringhe.

def user_integer_list_filler(list1):
    flaglister = True
    print("Aggiungi un intero [0:9] alla lista: ")
    while flaglister:
        answ = input()
        if answ == "N" or answ == "No" or answ == "NO" or answ == "n" or answ == "no":
            flaglister = False
        else:
            try:
                int(answ)
                if int(answ) > 9:
                    print("Inserisci un numero valido da 0 a 9 o termina con N")
                else:
                    print(f"Il numero {answ} è stato aggiunto alla lista, per concludere digitare N, per continuare inserire un altro elemento")
                    list1.append(answ)
            except ValueError:
                print("Il numero inserito non è un intero, inserisci un numero valido o termina con N")


def list_integer_to_list_string(list1):
    lenght = len(list1)
    newlist = []
    for i in range(lenght):
        try:
            tmp = int(list1[i])
            newlist.append(numeri_string[tmp])
        except ValueError:
            print(f"Il numero {list1[i]} non è valido e verrà saltato.")
    return newlist

numeri_string = {1: "uno", 2: "due", 3: "tre", 4: "quattro", 5: "cinque", 6: "sei", 7: "sette", 8: "otto", 9: "nove", 0: "zero"}


list1 = []
user_integer_list_filler(list1)
newlist = list_integer_to_list_string(list1)
print(newlist)

"""