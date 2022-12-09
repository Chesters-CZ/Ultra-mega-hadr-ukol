import time

import mysql.connector

database = mysql.connector.connect(host="localhost", username="Chesters", password="root", database="hadr")

print(database)

cursor = database.cursor()

Ip = input("Zadejte požadovanou IP adresu ")
Ip = Ip.split(".")
if (Ip.__len__() == 4):
    Query = ("SELECT ip1.city, ip1.stateprov, ip1.country, ip1.ip_start, ip1.ip_end FROM dbip_lookup_educa ip1 " +
             "WHERE ip1.id in (" + (
                                    "SELECT ip41.id FROM dbip_lookup_educa ip41 " +
                                    "WHERE  (ip_start_1 < " + Ip[0] + " AND ip_end_1 > " + Ip[0] + ")"
                                    ) + ")" +

             "OR ip1.id in (" + (
                                "SELECT ip32.id FROM dbip_lookup_educa ip32 " +
                                "WHERE ip32.id in (" + (
                                                        "SELECT ip42.id FROM dbip_lookup_educa ip42 " +
                                                        "WHERE (ip_start_1 = " + Ip[0] + " OR ip_end_1 = " + Ip[0] + ")"
                                                      ) + ") " +
                                "AND (ip32.ip_start_2 < " + Ip[1] + " AND ip32.ip_end_2 > " + Ip[1] + ")"
                                ) + ")" +
                                    # Pocaď done
             "OR ip1.id in (" + (
                                     "SELECT ip2.id FROM dbip_lookup_educa ip2 " +
                                     "WHERE ip2.id in (" + (
                                                            "SELECT ip3.id FROM dbip_lookup_educa ip3 " +
                                                            "WHERE ip3.id in (" + (
                                                                                    "SELECT ip4.id FROM dbip_lookup_educa ip4 " +
                                                                                    "WHERE  (ip_start_1 <= " + Ip[0] + " AND ip_end_1 >= " + Ip[0] + ")"
                                                                                  ) + ")"
                                                            ) + ")"
                                    ) + ")" +
             "OR ip1.id in (" + (
                     "SELECT ip2.id FROM dbip_lookup_educa ip2 " +
                     "WHERE ip2.id in (" + (
                             "SELECT ip3.id FROM dbip_lookup_educa ip3 " +
                             "WHERE ip3.id in (" + (
                                     "SELECT ip4.id FROM dbip_lookup_educa ip4 " +
                                     "WHERE  (ip_start_1 <= " + Ip[0] + " AND ip_end_1 >= " + Ip[0] + ")"
                             ) + ")"
                     ) + ")"
             ) + ")"
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
