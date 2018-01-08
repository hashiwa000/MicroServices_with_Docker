# MicroServices with Docker

## Prepare Your System

Install docker.

## How to Run

### Build containers

```
$ sudo docker build -t postgresql_sample postgresql
$ sudo docker build -t wsgi_sample wsgi_app
```

### Run containers

1) Run PostgreSQL and Insert data

```
$ sudo docker run -d -e POSTGRES_PASSWORD=hashiwa0 -p 5432:5432 --name postgres_instance postgresql_sample
$ python tools/create_records.py -p hashiwa0
```

2) Run WSGI Application

```
$ sudo docker run -d -p 8000:80 --link postgres_instance:postgres001 -e DBHOST=postgres001 -e DBPASSWORD=hashiwa0 wsgi_sample
```

3) See http://localhost:8000 at your browser.

