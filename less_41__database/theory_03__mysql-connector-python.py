"""
Пример использования библиотеки mysql-connector-python

Установка: pip install mysql-connector-python

Возможны проблемы с установкой на Windows.
Рекомендация: "откатить" более старую версию пакета, например:

pip uninstall mysql-connector-python
pip install mysql-connector-python==9.3.0

Если не поможет - следует "опуститься" ещё "ниже".
"""

import mysql.connector
from local_settings import dbconfig

# ⚠️ Таким образом мы легко можем поменять имя дефолтной БД на любое другое:
# было world, стало hr
dbconfig['database'] = 'hr'

connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()

cursor.execute("SELECT * FROM employees WHERE department_id = 30")
print(*cursor.fetchall(), sep="\n")


cursor.close()
connection.close()