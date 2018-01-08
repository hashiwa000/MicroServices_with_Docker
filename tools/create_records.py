import argparse

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import ProgrammingError

def create_database(conf):
    try:
        conn = psycopg2.connect("dbname=postgres host=%(host)s user=%(user)s password=%(password)s" % conf)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("CREATE DATABASE test;")
        cur.close()
        conn.commit()
    except ProgrammingError:
        pass # database "test" already exists

def create_records(conf):
    conn = psycopg2.connect("dbname=%(dbname)s host=%(host)s user=%(user)s password=%(password)s" % conf)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS records (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute("INSERT INTO records (num, data) VALUES (100, 'abc');")
    cur.execute("INSERT INTO records (num, data) VALUES (101, 'def');")
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dbname', '-d', default='test')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--user', '-u', default='postgres')
    parser.add_argument('--password', '-p', default='mysecretpassword')
    args = parser.parse_args()
    conf = {
            'dbname': args.dbname,
            'host': args.host,
            'user': args.user,
            'password': args.password,
            }
    create_database(conf)
    create_records(conf)

