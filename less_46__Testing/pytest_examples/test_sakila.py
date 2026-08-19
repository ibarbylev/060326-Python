import pytest
import mysql.connector
from local_settings import dbconfig


def test_connection():
    with mysql.connector.connect(**dbconfig) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

    assert result == (1,)


def test_get_films():
    with mysql.connector.connect(**dbconfig) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM sakila.film")
            result = len(cursor.fetchall())

    assert result == 1001