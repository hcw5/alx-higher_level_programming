#!/usr/bin/python3
"""
    Connects to a MySQL database.
    Gets data from `states` table.
    Prints the state names matching an argument.
"""
import MySQLdb
import sys


def main():
    """Prints state names matching argument, argv[4]"""
    username, password, db_name, state_name = sys.argv[1:]
    t_name = 'states'
    conn = None
    try:
        conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=db_name, charset='utf8'
        )
        with conn.cursor() as c:
            c.execute('USE {}'.format(db_name))
            q = 'SELECT * FROM {} WHERE name = "{}"'.format(t_name, state_name)
            c.execute(q)

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
