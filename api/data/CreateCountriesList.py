# reads in countries.csv file and creates list of all countries in data set
# exports list as a serializable object into countries.py

import pickle

countries = []

with open('countries.csv', 'rb') as csvData:
    for row in csvData:
        tokens = row.split(',')
        if tokens[0] == "People's Republic of China":
            countries.append("China")
        elif (tokens[0] == "Cote d'Ivoire (The Ivory Coast)"):
            countries.append("Cote d'Ivoire")
        else:
            countries.append(tokens[0])


csvData.close()
result = open('countries.py', 'wb')
pickle.dump(countries, result)
result.close()
