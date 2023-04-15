#!/usr/bin/python3
"""
-- Lists all states from the database hbtn_0e_0_usa
-- takes 3 arguments
-- module: MySQLdb
-- Connects to a MySQL server running on localhost at port 3306
-- Results sorted in ascending order by states.id
-- Code should not be executed when imported

"""
import MySQLdb
import sys


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cusor = db.cursor()
    cusor.execute("SELECT * FROM states")
    the_rows = cusor.fetchall()
    for row in the_rows:
        print(row)
    cusor.close()
    dtb.close()

