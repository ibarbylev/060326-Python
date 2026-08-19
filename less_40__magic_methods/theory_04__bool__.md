### Метод `__bool__`

Магический метод `__bool__` отвечает за булево значение объекта (`True` или `False`)
при использовании его в логическом контексте: `if`, `while`, `not` и других булевых выражениях.

---

**Синтаксис**

```python
class MyClass:
    def __bool__(self):
        # вернуть True или False
        return True  # или False
```

---

### Пример

```python
class Box:
    def __init__(self, items):
        self.items = items
    
    def __bool__(self):
        # объект пустой → False, есть элементы → True
        return bool(self.items)


empty_box = Box([])
full_box = Box([1, 2, 3])

print(bool(empty_box))  # False
print(bool(full_box))   # True

if full_box:
    print("Коробка не пуста!")


# False
# True
# Коробка не пуста!
```

---

### Почему функция `bool()` работает даже когда нет метода `__bool__()`?

Рассмотрим пример:
```python
class F:
    pass


f = F()

print(bool(f))  # True
try:
    print(f.__bool__())
except AttributeError as e:
    print(e)   # 'F' object has no attribute '__bool__'
```

Дело в том, что `bool()` не делает `f.__bool__()`.  

Алгоритм поиска здесь немного иной:
вместо метода `f.__bool__()` функция  `bool()` запускает встроенную функцию `PyObject_IsTrue()`,  
которая работает по следующему алгоритму:

1. Если у типа есть метод `__bool__()`  — вызвать его.
2. Иначе, если есть метод `__len__()` — вызвать его.
3. Иначе вернуть `True`.

Сильно упрощённо логику работы можно описать примерно так:

```python
def pseudo_bool(obj):
    if hasattr(type(obj), "__bool__"):
        return type(obj).__bool__(obj)
    elif hasattr(type(obj), "__len__"):
        return type(obj).__len__(obj) != 0
    else:
        return True
```

    На самом деле внутри CPython вместо `hasattr` используются слоты типа (`nb_bool`, `sq_length` и т.д.).  
    Но их поведение очень похоже на `hasattr`


Подобный алгоритм работает для специальных методов (`__len__`, `__iter__`, `__add__`, `__getitem__` и др.),  
связанных с функциями (и / или операторами) `len()`, `iter()`, `+`, `[]`, `in`, `not in` и др.

Интерпретатор ищет их на уровне типа, а не через обычный поиск атрибутов экземпляра.  
Это сделано ради производительности и чтобы поведение специальных операций было предсказуемым.

