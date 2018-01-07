import psycopg2

conf = {
        'dbname': 'test',
        'host': 'postgres001',
        'user': 'postgres',
        'password': 'mysecretpassword',
        'table': 'records',
       }

def get_records():
    cnn = psycopg2.connect("dbname=%(dbname)s host=%(host)s user=%(user)s password=%(password)s" % conf)
    cur = cnn.cursor()
    cur.execute("SELECT * FROM %(table)s;" % conf)
    return cur.fetchall()

def application(environ, start_response):
    records = get_records()
    status = '200 OK'
    output = str(records)

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
