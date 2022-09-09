#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                             <database name>
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 3306
    MY_USER = argv[1]
    MY_PSWD = argv[2]
    MY_DB = argv[3]
    db = MySQLdb.connect(host=HOST, user=MY_USER, password=MY_PSWD,
                         db=MY_DB, port=PORT)
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    rowquery = cur.fetchall()
    for qprint in rowquery:
        print(qprint)
    cur.close()
    db.close()
