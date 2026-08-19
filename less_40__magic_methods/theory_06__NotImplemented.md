Для арифметических операторов и операторов сравнения рекомендуется применять `NotImplemented`.

## 1. Арифметические операторы

### Как происходит поиск альтернативы?

Для выражения `a + b` Python действует по следующему алгоритму:

1. Пытается выполнить `a.__add__(b)`
2. Если вернул `NotImplemented` -> `b.__radd__(a)` 
3. Если снова `NotImplemented` -> `TypeError` 

ААналогичный механизм используется большинством бинарных арифметических операторов.

| Оператор | Основной метод | Обратный метод  |
| -------- | -------------- | --------------- |
| `+`      | `__add__`      | `__radd__`      |
| `-`      | `__sub__`      | `__rsub__`      |
| `*`      | `__mul__`      | `__rmul__`      |
| `/`      | `__truediv__`  | `__rtruediv__`  |
| `//`     | `__floordiv__` | `__rfloordiv__` |
| `%`      | `__mod__`      | `__rmod__`      |
| `**`     | `__pow__`      | `__rpow__`      |

---

## 2. Операторы сравнения

### Как происходит поиск альтернативы?

Здесь всё немного иначе.

Обратных методов (`__req__`, `__rlt__` и т.п.) не существует.

Поэтому, для `a < b` Python работает по алгоритму:
1. `a.__lt__(b)`
2. Если получен `NotImplemented`, то вызывает `b.__gt__(a)`.

То есть при неудаче вызывается **не обратный метод**, а **противоположный оператор**.

---

## 3. Где ещё есть обработка `NotImplemented`?`

Есть ещё у битовых операторов и у матричного умножения, но это уже совсем за пределами курса.

---

### Таблица альтернатив

| Выражение | Сначала       | Затем         |
| --------- | ------------- | ------------- |
| `a < b`   | `a.__lt__(b)` | `b.__gt__(a)` |
| `a <= b`  | `a.__le__(b)` | `b.__ge__(a)` |
| `a > b`   | `a.__gt__(b)` | `b.__lt__(a)` |
| `a >= b`  | `a.__ge__(b)` | `b.__le__(a)` |
| `a == b`  | `a.__eq__(b)` | `b.__eq__(a)` |
| `a != b`  | `a.__ne__(b)` | `b.__ne__(a)` |


---

## Резюме

| Арифметика                                                      | Сравнение                                                                                                                                                |
| --------------------------------------------------------------- |----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Есть методы `__r...__`                                          | Методов `__r...__` нет                                                                                                                                   |
| После `NotImplemented` вызывается `__radd__`, `__rsub__` и т.д. | После `NotImplemented` вызывается соответствующий метод второго операнда (`__gt__`, `__lt__`, `__eq__` и т.д.)                                           |
| Если никто не обработал операцию → `TypeError`                  | Если никто не обработал сравнение, тогда обычно возвращается: <br>для `==` → `False`, <br>для `!=` → `True`,<br>для остальных операторов → `TypeError`). |

---

### Пример 1. СЛОЖЕНИЕ между пользовательским и базовыми классами (`int`, `float`)

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"M({self.amount})"

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        if isinstance(other, (int, float)):
            return Money(self.amount + other)
        return NotImplemented

    def __radd__(self, other):
        # Вызывается, когда слева стоит обычное число:
        # 10 + m
        return self.__add__(other)   # сложение коммутативно


m = Money(10)

print(m + 5)    # M(15)   <- сработал __add__
print(5 + m)    # M(15)   <- сработал __radd__
print(m + m)    # M(20)   <- сработал __add__
```

---

### Пример 2. СЛОЖЕНИЕ между двумя пользовательскими классами

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"M({self.amount})"

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)


class Currency:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"C({self.amount})"

    def __add__(self, other):
        # Currency + Money
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __radd__(self, other):
        # Money + Currency  (вызывается, когда слева Money)
        if not isinstance(other, Money):
            return NotImplemented
        return Money(other.amount + self.amount)


m = Money(10)
c = Currency(5)

print(m + c)    # M(15)   <- сработал Currency.__radd__
print(c + m)    # M(15)   <- сработал Currency.__add__
```

---

### Пример 3. СРАВНЕНИЕ между пользовательским и базовыми классами (`int`, `float`)

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"M({self.amount})"

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.amount < other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.amount > other
        return NotImplemented


m = Money(10)

print(m < 20)    # True   <- сработал Money.__lt__
print(20 < m)    # False  <- Money.__lt__ -> NotImplemented -> Money.__gt__(20)
print(m > 5)     # True   <- сработал Money.__gt__
print(5 > m)     # False  <- Money.__gt__ -> NotImplemented -> Money.__lt__(5)
```

---

### Пример  4. СРАВНЕНИЕ между двумя пользовательскими классами

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"M({self.amount})"

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.amount < other.amount
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money):
            return self.amount > other.amount
        return NotImplemented


class Currency:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"C({self.amount})"

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.amount < other.amount
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money):
            return self.amount > other.amount
        return NotImplemented


m = Money(10)
c = Currency(5)

print(m < c)     # False  <- Money.__lt__ -> NotImplemented -> Currency.__gt__(m)
print(c < m)     # True   <- сработал Currency.__lt__
print(m > c)     # True   <- Money.__gt__ -> NotImplemented -> Currency.__lt__(m)
print(c > m)     # False  <- сработал Currency.__gt__
```