## Что такое `__dict__`?

`__dict__` — это магический атрибут, возвращающий словарь, 
в котором объект хранит свои атрибуты.

Пример:

```python
from pprint import pprint

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)

# ------ Для экземпляра класса: -------
print(p.__dict__)

# {'name': 'Alice', 'age': 30}


# ------  Для самого класса: -------
pprint(Person.__dict__)

# mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
#               '__doc__': None,
#               '__init__': <function Person.__init__ at 0x7fe1cd16a2a0>,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'Person' objects>})
```

---

## Для чего используется `__dict__`?

### 1. Инспекция атрибутов

Удобно для отладки:

```python
print(vars(p))
```

`vars(p)` = `p.__dict__`.

---

### 2. Динамическое изменение атрибутов

```python
p.__dict__['age'] = 31
print(p.age)  # 31
```



