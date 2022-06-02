#pip3 install mysql-connector-python

import mysql.connector as connector

cnx = connector.connect(
    host="127.0.0.1",
    user="joe",
    password="joe123",
    database="joedb"
)

cursor = cnx.cursor()

cursor.execute("select nom from items order by nom")

for i, (nom,) in enumerate(cursor):
    print(f"{i} => {nom}")

cursor.close()
cnx.close()
