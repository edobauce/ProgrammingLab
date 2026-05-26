import os

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        superlist = []
        try:
            with open(self.name, "r") as datafile:
                for line in datafile:
                    element1, element2 = line.strip().split(',')
                    try:
                        if element2 == "":
                            sublist = [element1, None]
                            superlist.append(sublist)
                        else:
                            sublist = [element1, float(element2)]
                            superlist.append(sublist)
                    except ValueError:
                            if len(superlist) > 1:
                                print('Errore nei valori')
                return(superlist)
        except Exception as generic_e:
            raise ExamException(f'Errore {generic_e}')
        
def cumpute_variations(time_series, first_year, last_year):
    if first_year > last_year or first_year == last_year:
        return("L'intervallo non è valido")
    else:
        interval_dict = {}
        first_year_mean = None
        last_year_mean = None
        current = first_year
        value = 0
        for i in range(len(time_series)):
            year, month = time_series[i][0].split('-')
            print(type(year))
            if int(year) == int(current):
                value += time_series[i][1]
                print(value)
                print(year)
                print(month)
            if month == "01" and time_series[i][1] != None and first_year_mean == None:
                first_year_mean = value / 12
                value = 0
                current += 1
            if month == "01" and time_series[i][1] != None and last_year_mean == None:
                last_year_mean = value / 12
                value = 0
                interval_dict[f"{(current-1)}-{current}"] = last_year_mean - first_year_mean
                first_year_mean = last_year_mean
                last_year_mean = None
                current += 1
            if current > last_year:
                break
    return interval_dict


csv_file = CSVTimeSeriesFile("data.csv")
time_series = csv_file.get_data()
print(cumpute_variations(time_series, 1953, 1959))
