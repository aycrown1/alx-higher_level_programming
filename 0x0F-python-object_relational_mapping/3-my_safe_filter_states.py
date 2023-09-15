#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states
               table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) == 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        dbase = sys.argv[3]
        searched = sys.argv[4]
        db = MySQLdb.connect(host='localhost', user=user, passwd=passwd,
                             db=dbase, port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        table = cursor.fetchall()
        for state in table:
            if state[1] == searched:
                print(state)
        cursor.close()
        db.close()
