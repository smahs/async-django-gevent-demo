# async-django-gevent-demo
An example async setup with Django, Gunicorn, Gevent and Psycopg2

Adapted from [kljensen](https://github.com/kljensen)'s [async-flask-sqlalchemy-example](https://github.com/kljensen/async-flask-sqlalchemy-example)

### Setup
- Install Python and Postgres from your distro's repos. Refer your distro's docs for this.
- Clone this repo, setup the virtual environment and fetch the requirements.
```bash
> virtualenv -p /usr/bin/python2 .env
> source .env/bin/activate
> python setup.py develop
# OR
> pip install -r requirements.txt
```
- Create the database in postgres.
```bash
> createdb djtest
```

### Run
Open two terminals and run the django app in one and test it on the other.
```bash
gunicorn project.wsgi:application -c gunicorn.conf
```
```bash
> python client.py
Sending 5 requests for http://127.0.0.1:8000/sleep_python...
	@  5.01s got response [200]
	@  5.01s got response [200]
	@  5.01s got response [200]
	@  5.01s got response [200]
	@  5.01s got response [200]
	=  5.02s TOTAL
Sending 5 requests for http://localhost:8000/sleep_psycopg2...
	@  5.02s got response [200]
	@  5.02s got response [200]
	@  5.02s got response [200]
	@  5.02s got response [200]
	@  5.03s got response [200]
	=  5.03s TOTAL
------------------------------------------
SUM TOTAL = 10.04s
```

### Pooling, and the lack of it
Unlike SQLAlchemy, Django [does not maintain](https://groups.google.com/forum/#!topic/django-developers/NwY9CHM4xpU) a connection pool by default. It does however support [persistent connections](https://docs.djangoproject.com/en/1.6/ref/databases/#persistent-connections).

In this particular case, sending a hundred concurrent requests with `python client.py 100` will open a hundred new connections, which can be very costly in production.

In production, using a connection pool is a good idea.
