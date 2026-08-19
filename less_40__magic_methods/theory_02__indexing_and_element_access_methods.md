## Методы индексации и доступа к элементам

### Содержание

| № | Метод                       | Назначение                       | 
|---|-----------------------------|----------------------------------|
| 1 | [`__getitem__`](#getitem)   | Чтение элемента `obj[key]`       |           
| 2 | [`__setitem__`](#setitem)   | Присваивание `obj[key] = value`  |         
| 3 | [`__delitem__`](#delitem)   | Удаление `del obj[key]`          |
| 4 | [`__len__`](#len)           | Длина объекта `len(obj)`         | 
| 5 | [`__contains__`](#contains) | Проверка `item in obj`           | 
| 6 | [Срезы (`slice`)](#slicing) | Обработка срезов в `__getitem__` | 


<a id="getitem"></a>
### 1. `__getitem__(self, key)`

Используется для чтения элемента `key` в объекте (коллекции) `obj`:

```python
obj[key]
```

**Пример:**

```python
class Vector:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

v = Vector([10, 20, 30])
print(v[1])  # 20
```

Метод поддерживает индексы, slicing и любые ключи.

---

<a id="setitem"></a>
### 2. `__setitem__(self, key, value)`

Используется для присваивания:

```python
obj[key] = value
```

**Пример:**

```python
def __setitem__(self, index, value):
    self.data[index] = value
```

---

<a id="delitem"></a>
### 3. `__delitem__(self, key)`

Удаляет элемент:

```python
del obj[key]
```

**Пример:**

```python
def __delitem__(self, index):
    del self.data[index]
```

---

<a id="len"></a>
### 4. `__len__(self)`

Возвращает длину объекта:

```python
len(obj)
```

**Пример:**

```python
def __len__(self):
    return len(self.data)
```

---

<a id="contains"></a>
### 5. `__contains__(self, item)`

Отвечает за оператор `in`:

```python
def __contains__(self, item):
    return item in self.data
```


---

<a id="slicing"></a>
### 6. Срезы (`slicing`) — `slice` в `__getitem__`

Если поступает срез, Python передаёт объект `slice(start, stop, step)`.

```python
def __getitem__(self, key):
    if isinstance(key, slice):
        print(type(key), key)  # <class 'slice'> slice(1, 4, None)
        return Vector(self.data[key])
    return self.data[key]
```

Если в `key` содержится диапазон — создаём и возвращаем новый объект `Vector`.  
Иначе возвращаем значение по индексу.

---

### Все методы сразу

```python
class Vector:
    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, key):
        if isinstance(key, slice):
            print(type(key), key)  # <class 'slice'> slice(1, 4, None)
            return Vector(self.data[key])
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return f"Vector({self.data})"


# ==== Демонстрация всех методов ====================

print("=== 1. __getitem__ ===")
v = Vector([10, 20, 30, 40, 50])
print(v[1])          # 20
print(v[1:4])        # Vector([20, 30, 40])

print("\n=== 2. __setitem__ ===")
v = Vector([10, 20, 30])
v[1] = 99
print(v)             # Vector([10, 99, 30])
v[1:3] = [40, 50]
print(v)             # Vector([10, 40, 50])

print("\n=== 3. __delitem__ ===")
v = Vector([10, 20, 30, 40])
del v[1]
print(v)             # Vector([10, 30, 40])
del v[1:3]
print(v)             # Vector([10])

print("\n=== 4. __len__ ===")
v = Vector([10, 20, 30])
print(len(v))        # 3

print("\n=== 5. __contains__ ===")
v = Vector([10, 20, 30, 40])
print(20 in v)       # True
print(99 in v)       # False
print(15 not in v)   # True

print("\n=== 6. Срезы (slicing) ===")
v = Vector([0, 10, 20, 30, 40, 50, 60])
print(v[1:5])        # Vector([10, 20, 30, 40])
print(v[::2])        # Vector([0, 20, 40, 60])
print(v[::-1])       # Vector([60, 50, 40, 30, 20, 10, 0])

```



