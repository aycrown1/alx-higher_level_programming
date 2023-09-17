#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) == 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        dbase = sys.argv[3]
        db = MySQLdb.connect(host='localhost', user=user, passwd=passwd,
                             db=dbase, port=3306)

        cursor = db.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities, states WHERE states.id=cities.state_id \
                    ORDER BY cities.id ASC")
        table = cursor.fetchall()
        for state in table:
            print(state)
        cursor.close()
        db.close()
