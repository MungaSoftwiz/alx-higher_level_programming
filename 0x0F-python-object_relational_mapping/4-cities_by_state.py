#!/usr/bin/python3
""" Lists all cities of the database hbtn_0e_4_usa, ordered by city id. """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    [print(city) for city in cur.fetchall()]
