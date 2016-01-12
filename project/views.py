from django.http import HttpResponse
from django.db import connection
from time import sleep


def sleep_psycopg2(request):
    connection.cursor().execute('select pg_sleep(5)')
    return HttpResponse('\r\n')


def sleep_python(request):
    sleep(5)
    return HttpResponse('\r\n')
