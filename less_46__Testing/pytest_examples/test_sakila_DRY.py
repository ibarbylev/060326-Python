import pytest
import mysql.connector
from local_settings import dbconfig

# Создаём фикстуру подключения к БД
@pytest.fixture
def cursor():
    with mysql.connector.connect(**dbconfig) as connection:
        with connection.cursor() as cursor:
            yield cursor


def test_connection(cursor):
    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    assert result == (1,)


def test_get_films(cursor):
    cursor.execute("SELECT * FROM sakila.film")
    result = len(cursor.fetchall())

    assert result == 1001