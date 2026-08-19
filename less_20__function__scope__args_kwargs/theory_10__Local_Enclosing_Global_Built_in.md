### 4 уровня видимости: Local, Enclosing, Global, Built-in (LEGB)

В Python обычно выделяют 4 области видимости (scope), где могут находиться переменные:

#### 1. Local (локальная область видимости)

Переменные, созданные внутри функции. 
Доступны только внутри этой функции.

```python
def test():
   x = 10  # локальная переменная
   print(x)
```

#### 2. Enclosing scope (внешняя / `nonlocal` область видимости)

**Enclosing scope** — это область видимости внешней функции целиком для вложенной функции,  
кроме её собственной локальной области.

Для `Enclosing` обязательно существование ДВУХ функция
* внешней (`outer()`)
* и вложенной в неё внутренней функции (`inner()`)


```python
def outer():
    x = 10        # enclosing scope для inner
    print(x)      # enclosing scope для inner 
    def inner():
        y = 5  # local scope
        print(x)  # поиск идёт во внешнюю функцию

    inner()  # enclosing scope для inner
```

#### 3. Global scope (глобальная область видимости)
Переменные, объявленные на уровне модуля.
Доступны во всём файле.

```python
z = 30  # глобальная переменная

def show():
   print(z)
```

#### 4. Built-in scope (встроенная область видимости)

Имена, встроенные в Python: `print`, `len`, `range` и др.

```python
print(len("Python"))
```

Порядок поиска переменных называется правилом **LEGB**:

* **L** — Local
* **E** — Enclosing
* **G** — Global
* **B** — Built-in
