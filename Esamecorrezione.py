# NOME: EDOARDO - COGNOME: BAUCE - MATRICOLA: SM32A00015

import os # Nel caso il file non si trovi nella stessa directory dello script

class ExamException(Exception): # Generico errore
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name # Nome del file da aprire ( o path )
        try:
            open(self.name, "r")
        except:
            raise ExamException("Il nome del file è errato o il file non è presente")
        
    def get_data(self):
        superlist = [] # Creo una lista in cui saranno contenute tutte le coppie di del dataset
        with open(self.name, "r") as dataset: # Apro il file sotto il nome di dataset
            for line in dataset: # Per ogni linea del dataset
                element1, element2 = line.strip().split(",") # Tolgo \n e separo sulla , data e consumi, rinominandoli element1 ed element2
                try: # Controllo che il valore atteso ( element2 ) sia convertibile a float. Se possibile crea una sottolista di due elementi
                    sublist = [element1, float(element2)] 
                    superlist.append(sublist) # Inserisco la sottolista nella lista principale
                except:
                    pass # Altrimenti, passa. In questo modo viene saltata la prima riga e tutte le righe senza valori o con valori non interpretabili come float
        return superlist
    

def compute_annual_mean(time_series, first_year, last_year):
    try:
        current = int(first_year) 
        last_year = int(last_year) # Controllo che i due valori inseriti possano essere convertiti ad intero, altrimenti linea 61
        consumption_dict = {} # Inizializzo il dizionario
        value = 0.0
        month_number = 0 
        year_mean = 0 # Sfrutto un pò di flag per aiutarmi con la gestione degli indici nella lista
        for i in range(0,len(time_series)): # Guardo ogni elemento nella lista fornita alla funzione, in modo tale da non tralasciare nulla
            month, year = time_series[i][0].split("/") # Divido la prima parte MM/YYYY in MM e YYYY
            month = int(month) 
            year = int(year) # Ricontrollo che siano validi gli argomenti forniti, altrimenti linea 61
            if year == current and month_number < 13: # Controllo che guardi l'anno corrente e che non sfori il numero di mesi. Per questo esercizio questo caso non sarebbe necessario
                single_value = (time_series[i][1]) # Prendo il valore di un mese nell'anno
                value = value + single_value # Lo sommo al totale dei valori dell'anno corrente
                month_number = month_number + 1 # Incremento il mese ( non sapendo se ogni mese viene contato nell'anno ho bisogno di conoscerne il numero per la media )
            if year != current and year > first_year: # In questo blocco calcolo la media, reimposto le varie flags ed inserisco tutto nel dizionario oppure ( line 55 )
                year_mean = round((value / month_number), 2)
                value = 0
                month_number = 0
                consumption_dict[f"{current}"] = {year_mean}
                single_value = (time_series[i][1]) # Cambiando i valori delle flag in questo blocco, eseguo il conto del primo mese che altrimenti verrebbe saltato
                value = value + single_value
                month_number = month_number + 1
                current = current + 1
            elif year == last_year: # Controllo, se l'anno corrente equivale all'ultimo anno, non reimposto le flags ma inserisco direttamente i valori
                year_mean = round((value / month_number), 2)
                consumption_dict[f"{current}"] = {year_mean}
            if current > last_year: # Mi assicuro che non esegua più alcuna aggiunta in caso il si vada oltre all'ultimo anno in input
                break
        return consumption_dict
    except:
        raise ExamException("Inserire valori interi o validi") 
    
    # L'eccezione scatta se qualsiasi delle operazioni nel blocco precedente non si può eseguire, comprendendo anche la somma o la divisione di variabili errate


gigio = CSVTimeSeriesFile("electricity.csv")
gigio_list = gigio.get_data()
print(compute_annual_mean(gigio_list, 2019, 2022))