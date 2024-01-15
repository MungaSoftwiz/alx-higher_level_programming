#!/usr/bin/python3
""" Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities as c\
                INNER JOIN states as s\
                ON c.state_id = s.id\
                ORDER BY c.id")
    print(", ".join([city[2] for city in cur.fetchall() if
                    city[4] == argv[4]]))
