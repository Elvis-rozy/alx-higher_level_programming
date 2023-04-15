#!/usr/bin/python3
"""
-- Lists all states from the database hbtn_0e_0_usa
-- takes 3 arguments
-- module: MySQLdb
-- Connects to a MySQL server running on localhost at port 3306
-- Results sorted in ascending order by states.id
-- Code should not be executed when imported

"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursr = con.cursor()
    cursr.execute("SELECT * FROM states ORDER BY id ASC")
    dtb = cursr.fetchall()
    for dt in dtb:
        print(dt)
    cursr.close()
    dtb.close()
