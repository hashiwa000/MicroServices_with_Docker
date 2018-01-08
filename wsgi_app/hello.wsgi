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
    with psycopg2.connect("dbname=%(DBNAME)s host=%(DBHOST)s user=%(DBUSER)s password=%(DBPASSWORD)s" % conf) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM %(DBTABLE)s;" % conf)
            row = cur.fetchone()
            while row is not None:
                yield row
                row = cur.fetchone()

def create_record_table():
    records = get_records()
    output = ''
    output += '<html>'
    output += '<header>'
    output += '<title>MicroService with Docker</title>'
    output += '</header>'
    output += '<body>'
    output += '<table border="1">'
    output += '<tr>'
    output += '<th>ID</th>'
    output += '<th>Number</th>'
    output += '<th>Data</th>'
    output += '</tr>'
    for record in records:
        output += '<tr>'
        output += '<td>' + str(record[0]) + '</td>'
        output += '<td>' + str(record[1]) + '</td>'
        output += '<td>' + str(record[2]) + '</td>'
        output += '</tr>'
    output += '</table>'
    output += '</body>'
    output += '</html>'
    return output


def application(environ, start_response):
    status = '200 OK'
    output = create_record_table()

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
