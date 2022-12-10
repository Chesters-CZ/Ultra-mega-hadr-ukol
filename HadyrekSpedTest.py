import random
import time

import mysql.connector

database = mysql.connector.connect(host="localhost", username="Chesters", password="root", database="hadr")

print(database)
print()
input("enter to begin")
print("begin!")

cursor = database.cursor()

times = []
try:
    while True:
        Imput = (random.randint(0, 255).__str__() + "." + random.randint(0, 255).__str__() + "." +
                 random.randint(0, 255).__str__() + "." + random.randint(0, 255).__str__()
                 )

        SplitIp = Imput.split(".")
        while True:
            print(Imput)
            Imput = (int(SplitIp[0]) * 1000000000 + int(SplitIp[1]) * 1000000 + int(SplitIp[2]) * 1000 + int(
                SplitIp[3])).__str__()
            Query = ("SELECT dbs.city, dbs.stateprov, dbs.country, dbs.ip_start, dbs.ip_end FROM dbip_lookup_educa dbs " +
                     "WHERE dbs.ip_start_dotless <= " + Imput + " AND dbs.ip_end_dotless >= " + Imput + " " +
                     "LIMIT 1"
                     )
            TimeStart = time.time()
            cursor.execute(Query)
            TimeEnd = time.time()
            print("execution finished (" + str(TimeEnd - TimeStart) + "s)")
            if (TimeEnd - TimeStart >= 0.25):
                time.sleep(10)
                print("unsatisfactory processing time, trying again...")
                cursor.fetchall()
            else:
                break
        times.append(TimeEnd - TimeStart)
        print("Average of " + len(times).__str__() + " attempts is " + (sum(times) / len(times)).__str__() + "s")
        for row in cursor.fetchall():
            print(row)
            for cell in row:
                time.sleep(0)
                # print(cell)
        print()

except KeyboardInterrupt as e:
    print()
    print("-- CTRL+C received --")
    print("Average of " + len(times).__str__() + " attempts is " + (sum(times) / len(times)).__str__() + "s")
except Exception as e:
    print()
    print("!! Something went wrong !!")
    print(e.args)
    print("Average of " + len(times).__str__() + " attempts is " + (sum(times) / len(times)).__str__() + "s")