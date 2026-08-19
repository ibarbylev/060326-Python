## SQL‑инъекции

Вариантов инъекция может быть множество.  

И эффект от их воздействия тоже располагается в очень широком диапазоне:
* от **"посмотреть чуть дальше, чем разрешается"**,
* до **"полного удаления (изменения) всех данных"**.

В примере ниже рассмотрен самый "безобидный" вариант:

В условие `WHERE Name = city_name` вместе с городом подставляется `OR 1 = 1`.  

Что фактически превращает запрос 
* из `SELECT * FROM world.city WHERE Name = 'Berlin'`
  * (то есть **"покажи одну строчку таблицы"**).
* в `SELECT * FROM world.city WHERE true`. 
  * (то есть **"покажи всю таблицу целиком"**).

### Опасный вариант (данные напрямую)

```python
import mysql.connector
from local_settings import dbconfig

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        city_name = "Berlin' OR '1'='1"
        query = f"SELECT * FROM world.city WHERE Name = '{city_name}'"
        cursor.execute(query)
        print(f"Запрос содержит {len(cursor.fetchall())} строк данных")

        # Запрос содержит 4079 строк данных
```

* Ввод превращается в часть SQL‑кода.
* Может вернуть все строки или удалить данные.

### Безопасный вариант (параметризованные запросы)

```python
        city_name = "'Berlin' OR 1 = 1"
        query = "SELECT * FROM world.city WHERE Name = %s"
        cursor.execute(query, (city_name,))
        print(f"Запрос содержит {len(cursor.fetchall())} строк данных")

        # Запрос содержит 0 строк данных
```

* Ввод обрабатывается как обычная строка.
* SQL‑код не изменяется.

