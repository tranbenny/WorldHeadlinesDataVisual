# create database configuration
# create a read method
# format read method into json format

import sys
sys.path.insert(0, './data')

import databaseConfig as db
import time
try:
    import mysql.connector
except:
    print("make sure mysql-connector-python is installed, install from mysql site")


def readFromDatabase():
    todayDate = time.strftime('%Y-%m-%d')
    print(todayDate)
    # todayDate = '2016-04-05'
    connection = mysql.connector.connect(user=db.user, password=db.password, host=db.host, database=db.database)
    cursor = connection.cursor(buffered=True)
    query = "SELECT * FROM " + db.TABLE_NAME + " WHERE HEADLINE_DATE = '" + todayDate + "';"
    cursor.execute(query)
    print(cursor)
    results = []
    for (HEADLINE_DATE, TITLE, COUNTRIES, PUBLISHED_DATE, DESCRIPTION, SOURCE) in cursor:
        countries = COUNTRIES.split("|")
        article = {
            'date': str(HEADLINE_DATE),
            'title' : TITLE,
            'countries' : countries,
            'source' : SOURCE
        }
        results.append(article)

    cursor.close()
    connection.close()
    return results
