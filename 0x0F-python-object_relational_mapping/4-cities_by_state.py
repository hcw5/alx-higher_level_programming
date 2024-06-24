#!/usr/bin/python3
"""
    Connects to a MySQL database, `hbtn_0e_4_usa`.
    Retrieves data from tables; `cities`, `states`.
    Prints cities by state.
"""
import MySQLdb
import sys


def main():
    username, password, db_name = sys.argv[1:]
    conn = None
    try:
        conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=db_name, charset='utf8'
        )
        with conn.cursor() as c:
            q = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id;
                """
            c.execute(q)

            res = c.fetchall()
            for row in res:
                print(row)
    except MySQLdb.Error as err:
        print(f'Error: {err}')
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    main()
