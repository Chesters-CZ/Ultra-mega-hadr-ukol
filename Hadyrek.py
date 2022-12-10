import numbers
import time

import mysql.connector

database = mysql.connector.connect(host="localhost", username="Chesters", password="root", database="hadr")

print(database)

cursor = database.cursor()

Imput = input("Zadejte požadovanou IP adresu ")
SplitIp = Imput.split(".")

if (SplitIp.__len__() == 4):
    Imput = (int(SplitIp[0]) * 1000000000 + int(SplitIp[1]) * 1000000 + int(SplitIp[2]) * 1000 + int(
        SplitIp[3])).__str__()
    print(Imput)
    Query = ("SELECT dbs.city, dbs.stateprov, dbs.country, dbs.ip_start, dbs.ip_end FROM dbip_lookup_educa dbs " +
             "WHERE dbs.ip_start_dotless <= " + Imput + " AND dbs.ip_end_dotless >= " + Imput + " " +
             "LIMIT 1"
             )
    TimeStart = time.time()
    cursor.execute(Query)
    TimeEnd = time.time()
    print("execution finished (" + str(TimeEnd - TimeStart) + "s)")

    for row in cursor.fetchall():
        print(row)
        for cell in row:
            time.sleep(0)
            # print(cell)
    print()
