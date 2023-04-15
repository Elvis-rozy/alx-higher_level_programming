#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
script that lists all states from the database

'''
if __name__ == "__main__":
    cont = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursr = cont.cursor()
    cursr.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (argv[4],)
        )
    dtb = cursr.fetchall()
    for dt in dtb:
        print(dt)

