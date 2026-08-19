## Способы передачи значений в SQL‑запросы 

---

### 1. Вставка значений в f-string

```python
city_name = "Moscow"
query = f"SELECT * FROM city WHERE Name = '{city_name}'"
cursor.execute(query)
```

* Допустима ТОЛЬКО для динамических идентификаторов, например 
  * имён таблиц или столбцов.
* КАТЕГОРИЧЕСКИ НЕ рекомендуется для пользовательских данных 
  * (риск SQL‑инъекций, ошибки с кавычками).

---

### 2. Параметризованные запросы

#### 2.1. Плейсхолдеры `%s` (тюпл)

```python
city_name = "Moscow"
query = "SELECT * FROM city WHERE Name = %s"
cursor.execute(query, (city_name,))  # Запятая обязательна (это tuple)!!!
```

* Значение передаётся отдельно от SQL.
* Драйвер экранирует данные:
  * связывает переданные значения с параметрами SQL 
  * и преобразует Python-типы в формат, понятный MySQL
* Защита от SQL‑инъекций.

#### 2.2. Именованные параметры (`%(name)s`)

```python
params = {"city": "Moscow"}
query = "SELECT * FROM city WHERE Name = %(city)s"
cursor.execute(query, params)
```

* Можно передавать несколько параметров по именам.
* Удобно и безопасно для сложных запросов.


##### Пример с передачей нескольких параметров

```python
params = {"pop": 1000000, "code": "RUS"}
query = """
SELECT Name
FROM city
WHERE Population > %(pop)s AND CountryCode = %(code)s
"""
cursor.execute(query, params)
```

* Порядок не важен, важны имена параметров.
* Безопасно и удобно для динамических значений.

---

###  Примеры и анти-примеры передачи данных в запросы 

---

#### Пример 1: неудачная попытка передать динамический идентификатор как параметрический

Динамические идентификаторы (например, имя таблицы) нельзя передать как параметрические:

```python
import mysql.connector
from local_settings import dbconfig

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        data = {
            "table": "world.city",
            "pop": 1000000,
        }
        try:
            query = "SELECT * FROM %(table)s WHERE Population > %(pop)s LIMIT 10"
            cursor.execute(query, data)
            print(*cursor.fetchall(), sep="\n")

        except Exception as e:
            print(e)

            # ProgrammingError(1064, "1064 (42000):
            # You have an error in your SQL syntax;
            # check the manual that corresponds to your MySQL server version
            # for the right syntax to use near
            # '%s WHERE Population > %s LIMIT 10' at line 1"
```

#### Пример 2: для каждого типа параметров — свой способ передачи

Исправленный вариант (имя таблицы вставляем через `.format()` или `f-string`):

```python
import mysql.connector
from local_settings import dbconfig

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        data = {
            "table": "world.city",
            "pop": 1000000,
        }
        try:
            table = data["table"]
            params = {"pop": data["pop"]}
            query = f"SELECT * FROM {table} WHERE Population > %(pop)s LIMIT 10"
            cursor.execute(query, data)
            print(*cursor.fetchall(), sep="\n")

        except Exception as e:
            print(e)

            # (1, 'Kabul', 'AFG', 'Kabol', 1780000)
            # (35, 'Alger', 'DZA', 'Alger', 2168000)
            # (56, 'Luanda', 'AGO', 'Luanda', 2022000)
            # (69, 'Buenos Aires', 'ARG', 'Distrito Federal', 2982146)
            # (70, 'La Matanza', 'ARG', 'Buenos Aires', 1266461)
            # (71, 'Córdoba', 'ARG', 'Córdoba', 1157507)
            # (126, 'Yerevan', 'ARM', 'Yerevan', 1248700)
            # (130, 'Sydney', 'AUS', 'New South Wales', 3276207)
            # (131, 'Melbourne', 'AUS', 'Victoria', 2865329)
            # (132, 'Brisbane', 'AUS', 'Queensland', 1291117)
```

---

#### Пример 3: Анти-пример — всё вставляем через `.format()`


Можно пойти ещё дальше и всё вставить через формат.  
Работать будет, но это "грубейшее" нарушение безопасности!`

```python
import mysql.connector
from local_settings import dbconfig

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        data = {
            "table": "world.city",
            "pop": 1000000,
        }
        try:
            query = "SELECT * FROM {table} WHERE Population > {pop} LIMIT 10"
            cursor.execute(query.format(**data))
            print(*cursor.fetchall(), sep="\n")

        except Exception as e:
            print(e)

            # (1, 'Kabul', 'AFG', 'Kabol', 1780000)
            # (35, 'Alger', 'DZA', 'Alger', 2168000)
            # (56, 'Luanda', 'AGO', 'Luanda', 2022000)
            # (69, 'Buenos Aires', 'ARG', 'Distrito Federal', 2982146)
            # (70, 'La Matanza', 'ARG', 'Buenos Aires', 1266461)
            # (71, 'Córdoba', 'ARG', 'Córdoba', 1157507)
            # (126, 'Yerevan', 'ARM', 'Yerevan', 1248700)
            # (130, 'Sydney', 'AUS', 'New South Wales', 3276207)
            # (131, 'Melbourne', 'AUS', 'Victoria', 2865329)
            # (132, 'Brisbane', 'AUS', 'Queensland', 1291117)
```

**Таким образом**:

* **Идентификаторы не могут быть параметризованы**, 
  * поэтому для них используется `f-string` или `.format()`.
* Но данные следует передавать ТОЛЬКО через параметры,
  * чтобы запросы оставались безопасными.

⚠️ Важно помнить:
Если динамические идентификаторы приходят от пользователя,  
то они должны проходить дополнительную проверку через `whitelist`.  
(то есть сравниваться со списком разрешённых значений).

```python
ALLOWED_TABLES = {"city", "country", "countrylanguage"}
if data["table"] not in ALLOWED_TABLES:
    raise ValueError("Недопустимое имя таблицы")
```

---

### Итог

| Способ                            | Где безопасно         | Рекомендация                           |
|-----------------------------------| --------------------- |----------------------------------------|
| f-string / % форматирование       | Имена таблиц/столбцов | ✅ Можно, но только для идентификаторов |
| Прямая вставка данных в запрос    | ❌ Нет                 | ❌ Никогда для пользовательских данных  |
| Параметризованные (`%s`)          | ✅ Да                  | ✅ Всегда для данных                    |
| Именованные параметры (`%(pop)s`) | ✅ Да                  | ✅ Удобно, если данных много            |
