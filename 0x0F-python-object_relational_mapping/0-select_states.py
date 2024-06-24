#!/usr/bin/python3
"""Connects to a MySQL database. Gets data from a table. Prints the result."""
import MySQLdb
import sys


def main():
    username, password, db_name = sys.argv[1:]
    t_name = 'states'
    conn = None
    try:
        conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=db_name, charset='utf8'
        )
        with conn.cursor() as c:
            c.execute(f'USE {db_name}')
            c.execute(f'SELECT * FROM {t_name}')

            res = c.fetchall()
            for row in res:
                print(row)
    except MySQLdb.Error as err:
        print(f"Error: {err}")
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    main()
