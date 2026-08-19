### Правильное указание пути импорта (см. пример в [package_exampl_2](./package_example_2))

* Python ищет модули в списке `sys.path`, который формируется примерно так:

1. Директория текущего скрипта
2. PYTHONPATH (переменная окружения, указывающая дополнительные каталоги для поиска модулей)
3. Стандартные Python-библиотеки
4. Установленные пакеты в site-packages


#### Пример

```
project/
 ├── main.py
 ├── library/
 │   ├── __init__.py
 │   └── funcs.py
 ├── tests/
 │   ├── __init__.py
 │   └── test.py
```

* Импорт из внутренней папки `library`:

```python
# main.py
from library import funcs
funcs.greet1()
```

* либо

```python
from library.funcs import greet1
```


* Если `__init__.py` содержит промежуточный импорт:
```python
from .funcs import greet1  # импорт функции из соседнего модуля
```

* то импорт в `main.py` можно упростить:

```python
from library import greet1
```

### Проблема при запуске из внутреннего каталога

* Примеры выше прекрасно работают, если проект запускается через `main.py`
* ⚠️ Но если мы запустим тесты `tests/test.py`, то скорее всего получим `ImportError`

Варианты решений:
1. **Локальное** решение:
   * Изменить `Source root` в PyCharm с помощью `Mark Directory as -> Sources Root`
2. Один из вариантов **стабильного** решения:
   * [Добавить путь в `sys.path`](https://www.youtube.com/watch?v=6uWSmqZCz2o)


