#!/usr/bin/python3


def getAllStates(user2, passward2, db2, uinput):
    """ script that gets all the states when called on """
    import MySQLdb
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user2,
            passwd=passward2,
            db=db2,
            charset="utf8")
    cur = conn.cursor()
    cmd = """SELECT cities.name
            FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
            WHERE states.name = %s
            """
    cur.execute(cmd, (uinput,))
    rows = cur.fetchall()
    listo = []
    for row in rows:
        listo.append(row[0])
    print(", ".join(listo))
    cur.close()
    conn.close()
    # engine = sqlalchemy.create_engine()
    # db = MySQLdb.connect(host=MY_HOST, user=MY_USER, db=MY_DB)
    # cur = db.cursor()

if __name__ == "__main__":
    import sys
    """ protected from executing when imported """
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
