#!/usr/bin/python3
"""
    Connects to a MySQL db passed as an argument (argv[3]), `hbtn_0e_4_usa`.
    Retrieves data from tables; `cities`, `states`.
    Prints cities of the state passed as argument (argv[4]).
"""
import MySQLdb
import sys


def main():
    "Prints cities of the name of a state that is passed as an argument"
    username, password, db_name, state_name = sys.argv[1:]
    conn = None
    try:
        conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=db_name, charset='utf8'
        )
        with conn.cursor() as c:
            query = """
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                """
            c.execute(query, (state_name,))
            res = [item[0] for item in c.fetchall()]
            print(', '.join(res))
    except MySQLdb.Error as err:
        print(f'Error: {err}')
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    main()
