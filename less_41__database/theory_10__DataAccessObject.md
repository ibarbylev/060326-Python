Часто бывает удобно создать свой собственный контекстный менеджер.

Поскольку, в нём можно реализовать (и инкапсулировать!)
* не только управление соединением и курсором, 
* но и методы выполнения конкретных запросов.

Это часто называют **Data Access Object (DAO) стиль** — слой доступа к данным,  
где пользовательский класс инкапсулирует все запросы к базе.

---

### Пример расширенного класса с методами

```python
import mysql.connector
from mysql.connector import Error

from local_settings import dbconfig

# ---------------------------------
# Пользовательское исключение
# ---------------------------------
class DatabaseError(Exception):
    """Пользовательское исключение слоя доступа к данным"""

# ---------------------------------
# Базовый класс подключения 
# ---------------------------------
class MySQLConnection:
    """Контекстный менеджер для подключения к MySQL с поддержкой commit/rollback"""

    def __init__(self, db_config, autocommit: bool = False):
        self.dbconfig = db_config
        self.autocommit = autocommit
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.dbconfig)
        self.connection.autocommit = self.autocommit
        self.cursor = self.connection.cursor() 
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

    # -----------------------------
    # Методы выборки
    # -----------------------------
    def fetch_cities(self, limit=10):
        """Получить список городов"""
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
        try:
            self.cursor.execute(
                "INSERT INTO world.city (Name, CountryCode, Population) VALUES (%s, %s, %s)",
                (name, country_code, population)
            )
            # commit выполняется автоматически в __exit__
        except mysql.connector.Error as e:
            raise DatabaseError(f"Ошибка при добавлении города {name}") from e
```

---

### Пример использования

```python
with WorldDB(dbconfig, autocommit=True) as db:
    # Выборка городов
    cities = db.fetch_cities(limit=5)
    print("Города:", *cities, sep="\n")

with WorldDB(dbconfig, autocommit=True) as db:
    # Выборка страны
    country = db.fetch_country_by_code("USA")
    print("Страна:", country)

try:
    with WorldDB(dbconfig, autocommit=True) as db:
        # Добавление нового города
        db.add_city("NewCity", "USA", 12345)
        print("Город добавлен!")
except DatabaseError as e:
    print(f'{e.__class__.__name__}: {e}')
    print("Для использования этого метода требуется подключение с ПРАВАМИ НА ЗАПИСЬ!!!")
```

---

### Преимущества такого подхода

1. **Инкапсуляция всех запросов**

   * Код, который использует `WorldDB`, не знает SQL деталей — всё скрыто в методах класса.

2. **Централизованная обработка ошибок**

   * Все ошибки драйвера `mysql.connector` преобразуются в единое пользовательское исключение `DatabaseError`.

3. **Автоматический commit/rollback**

   * Логика транзакций реализована в базовом классе `MySQLConnection`:
     * надёжная работа с изменением данных без лишнего кода.

4. **Расширяемость через наследование**

   * Можно добавлять новые методы для любых операций в любых классах-наследниках, 
   * не меняя внешний код и не дублируя логику подключения.

5. **Следование правильным архитектурным рекомендациям (SOLID)**

   * SRP (разделение ответственности между базовым и специализированным классом)
   * DIP (бизнес-код не зависит от исключений конкретного драйвера)

6. **Каждая логически законченная операция имеет отдельное подключение**:
   * При сбое сети или ошибки “страдает” только эта операция, остальные остаются неизменными.
   * Для production-решений такой подход следует заменить на пул соединений (`connection pooling`) 
     * — это позволяет переиспользовать соединения и повышает производительность под нагрузкой.

---

### Зачем `return False` в методе `__exit__`?

В протоколе контекстного менеджера можно подавить (скрыть) исключение, которое произошло внутри блока `with`.

Как видим, метод 
```python 
def __exit__(self, exc_type, exc_value, traceback):
    pass
``` 
уже содержит 3 параметра исключения, которое может возникнуть внутри блока `with`:`
* `exc_type` — тип исключения;
* `exc_value` — значение исключения;
* `traceback` — трассировка исключения.

Соответственно:

* Если внутри блока не было исключения —> `exc_type = exc_value = traceback = None`.
* Если внутри блока было исключение —> все эти три аргумента будут содержать информацию об ошибке.

Поэтому возврат `True` или `False` из `__exit__` решает судьбу этого исключения:

1. `return True` (или любое истинное значение) —> исключение подавляется. 
  * Оно больше никуда не всплывает, программа продолжает работать так, будто ошибки не было.

2. `return False` (или None) → исключение не подавляется. 
  * После завершения `__exit__` оно будет выброшено дальше по стеку вызовов.