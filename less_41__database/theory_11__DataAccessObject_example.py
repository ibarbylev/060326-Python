from pprint import pprint

import mysql.connector
from mysql.connector import Error

from local_settings import dbconfig

# ---------------------------------
# Пользовательское исключение
# ---------------------------------
class DatabaseError(Exception):
    """Пользовательское исключение слоя доступа к данным"""
    pass

# ---------------------------------
# Базовый класс подключения
# ---------------------------------
class MySQLConnection:
    """Контекстный менеджер для подключения к MySQL с поддержкой commit/rollback"""

    def __init__(self, db_config, autocommit=False, is_dict=True):
        self.dbconfig = db_config
        self.autocommit = autocommit
        # определяет формат курсора: список словарей или список тюплов
        self.is_dict = is_dict
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.dbconfig)
        self.connection.autocommit = self.autocommit
        self.cursor = self.connection.cursor(dictionary=self.is_dict)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if not self.autocommit:
                if exc_type is None:
                    self.connection.commit()  # фиксируем изменения при отсутствии ошибок
                else:
                    self.connection.rollback()  # откат при ошибке

        except Error as exc:
            raise DatabaseError("Ошибка при завершении транзакции") from exc

        finally:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        return False  # не подавляем исключения

# ---------------------------------
# Специализированный класс для базы world
# ---------------------------------
class WorldDB(MySQLConnection):
    """Методы для работы с таблицами world.city и world.country"""

    def _ensure_cursor(self):
        """Метод проверки на случай, если методы будут вызваны вне контекстного менеджера"""
        if self.cursor is None:
            raise RuntimeError("Метод должен вызываться внутри блока with")

    # -----------------------------
    # Методы выборки
    # -----------------------------
    def fetch_cities(self, limit=10):
        """Получить список городов"""
        self._ensure_cursor()
        try:
            self.cursor.execute(
                "SELECT * FROM world.city LIMIT %s",
                (limit,)
            )
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            raise DatabaseError("Ошибка при выборке городов") from e

    def fetch_country_by_code(self, code):
        """Получить информацию о стране по коду"""
        self._ensure_cursor()
        try:
            self.cursor.execute(
                "SELECT * FROM world.country WHERE code=%s",
                (code,)
            )
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            raise DatabaseError(f"Ошибка при выборке страны с кодом {code}") from e

    # -----------------------------
    # Методы изменения данных
    # -----------------------------
    def add_city(self, name, country_code, population):
        """Добавить новый город"""
        self._ensure_cursor()
        try:
            self.cursor.execute(
                "INSERT INTO world.city (Name, CountryCode, Population) VALUES (%s, %s, %s)",
                (name, country_code, population)
            )
        except mysql.connector.Error as e:
            raise DatabaseError(f"Ошибка при добавлении города {name}") from e


if __name__ == "__main__":
    with WorldDB(dbconfig, is_dict=False) as db:
        # Выборка городов
        # is_dict=True, поэтому вывод будет в формате list[tuple]
        cities = db.fetch_cities(limit=5)
        print("Города:", *cities, sep="\n")

    with WorldDB(dbconfig, is_dict=True) as db:
        # Выборка страны
        # is_dict=True, поэтому вывод будет в формате list[dict]
        country = db.fetch_country_by_code("USA")
        print("Страна: USA")
        pprint(country)

    try:
        with WorldDB(dbconfig, autocommit=True) as db:
            # Добавление нового города
            db.add_city("NewCity", "USA", 12345)
            print("Город добавлен!")
    except DatabaseError as e:
        print(f'{e.__class__.__name__}: {e}')
        print("Для использования этого метода требуется подключение с ПРАВАМИ НА ЗАПИСЬ!!!")
