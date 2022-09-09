#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
Usage: ./4-cities_by_state.py <mysql username> \
                              <mysql password> \
                              <database name>
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 3306
    MY_USER = argv[1]
    MY_PSWD = argv[2]
    MY_DB = argv[3]
    db = MySQLdb.connect(host=HOST, user=MY_USER, password=MY_PSWD,
                         db=MY_DB, port=PORT)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
                    FROM cities \
                    INNER JOIN states \
                    ON cities.state_id = states.id \
                    ORDER BY cities.id ASC;"
    cur.execute(query)
    row_query = cur.fetchall()
    for rq_print in row_query:
        print(rq_print)
    cur.close()
    db.close()
