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
$ sudo docker run -d -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 --name postgresql_container postgresql_sample
$ python tools/create_records.py 
```

2) Run WSGI Application

```
$ sudo docker run -d -p 8000:80 --link postgresql_container:postgres001 wsgi_sample
```

3) See http://localhost:8000 at your browser.

