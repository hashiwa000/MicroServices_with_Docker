from os import getenv
import psycopg2

conf = {
        'DBNAME': getenv('DBNAME', 'test'),
        'DBHOST': getenv('DBHOST', 'postgres001'),
        'DBUSER': getenv('DBUSER', 'postgres'),
        'DBPASSWORD': getenv('DBPASSWORD', 'mysecretpassword'),
        'DBTABLE': getenv('DBTABLE', 'records'),
       }

def get_records():
    cnn = psycopg2.connect("dbname=%(DBNAME)s host=%(DBHOST)s user=%(DBUSER)s password=%(DBPASSWORD)s" % conf)
    cur = cnn.cursor()
    cur.execute("SELECT * FROM %(DBTABLE)s;" % conf)
    return cur.fetchall()

def application(environ, start_response):
    records = get_records()
    status = '200 OK'
    output = str(records)

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
