# reads in countries.csv file and creates list of all countries in data set

from pymongo import MongoClient

# add countries to collection in db
client = MongoClient('mongodb://localhost:8000')
db = client.country

countries = []

# tokens[0] = country name
# tokens[1] = 2-Letter country code
with open('countries.csv', 'r') as csvData:
    for row in csvData:
        tokens = row.split(',')
        name = tokens[0]
        country_code = tokens[1]
        if tokens[0] == "People's Republic of China":
            name = "China"
        elif (tokens[0] == "Cote d'Ivoire (The Ivory Coast)"):
            name = "Cote d'Ivoire"
        document = {
            "country_name" : name,
            "country_code" : country_code
        }
        db.countries.insert_one(document)
        countries.append(name)


csvData.close()


