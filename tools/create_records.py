import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import ProgrammingError

def create_database():
    try:
        conn = psycopg2.connect("dbname=postgres host=localhost user=postgres password=mysecretpassword")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("CREATE DATABASE test;")
        cur.close()
        conn.commit()
    except ProgrammingError:
        pass # database "test" already exists

def create_records():
    conn = psycopg2.connect("dbname=test host=localhost user=postgres password=mysecretpassword")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS records (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute("INSERT INTO records (num, data) VALUES (100, 'abc');")
    cur.execute("INSERT INTO records (num, data) VALUES (101, 'def');")
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    create_records()

