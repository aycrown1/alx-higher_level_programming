#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    data = cursor.fetchall()
    for state in data:
        if state[1][0] == 'N':
            print(state)
    cursor.close()
    db.close()
