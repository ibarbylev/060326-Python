## Методы проверки предиката

В программировании **предикат** — это функция/метод, которая возвращает логическое значение `True`/`False`

| Метод | Описание                                                                                          | Пример (✅ True)                      | Антипример (❌ False)                   |
|-------|---------------------------------------------------------------------------------------------------|--------------------------------------| -------------------------------------- |
| `isalpha()` | Проверяет, состоит ли строка <br> только из букв.                                                 | `"Привет".isalpha() → True`          | `"Hello123".isalpha() → False`         |
| `isdigit()` | Проверяет, состоит ли строка <br> только из цифр.                                                 | `"12345".isdigit() → True`           | `"12.3".isdigit() → False`             |
| `isalnum()` | Проверяет, состоит ли строка <br> только из букв и цифр.                                          | `"Python3".isalnum() → True`         | `"Hello!".isalnum() → False`           |
| `isspace()` | Проверяет, состоит ли строка <br> только из пробельных символов.                                  | `"   ".isspace() → True`             | `" a ".isspace() → False`              |
| `islower()` | Проверяет, все ли буквы <br> строки в нижнем регистре.                                            | `"python".islower() → True`          | `"Python".islower() → False`           |
| `isupper()` | Проверяет, все ли буквы <br> строки в верхнем регистре.                                           | `"HELLO".isupper() → True`           | `"Hello".isupper() → False`            |
| `istitle()` | Проверяет, каждое ли слово <br> начинается с заглавной буквы и продолжается строчными.            | `"Hello World".istitle() → True`     | `"Hello world".istitle() → False`      |
| `startswith()` | Проверяет, начинается ли строка <br> с указанной подстроки.                                       | `"Python".startswith("Py") → True`   | `"Python".startswith("on") → False`    |
| `endswith()` | Проверяет, заканчивается ли строка <br> указанной подстрокой.                                     | `"Python".endswith("on") → True`     | `"Python".endswith("Py") → False`      |
| `isdecimal()` | Проверяет, состоит ли строка <br> только из **десятичных** цифр.                                  | `"123".isdecimal() → True` <br> `"²".isdigit()  → True` | `"²".isdecimal() → False`              |
| `isnumeric()` | Проверяет, состоит ли строка <br> только из числовых символов <br> (в т.ч. дробей, римских цифр). | `"Ⅷ".isnumeric() → True`             | `"12.5".isnumeric() → False`           |
| `isascii()` | Проверяет, состоит ли строка <br> только из ASCII-символов (0–127).                               | `"Hello!".isascii() → True`          | `"Привет".isascii() → False`           |
| `isprintable()` | Проверяет, все ли символы <br> строки — печатаемые.                                               | `"Hello 123".isprintable() → True`   | `"Hello\nWorld".isprintable() → False` |
| `isidentifier()` | Проверяет, является ли строка <br> допустимым идентификатором в Python.                           | `"variable_1".isidentifier() → True` | `"1variable".isidentifier() → False`   |




## `isidentifier()`.

### Что такое идентификатор в Python

**Идентификатор** — это имя, которое можно использовать для:

* переменных,
* функций,
* классов,
* модулей и т.д.

Примеры идентификаторов:

```python
x
my_var
data123
_underscore
```

---

### Идентификатор в Python МОЖЕТ:

- Может содержать **буквы** (латиница, символы Unicode — например, кириллица).
- Может содержать **цифры**, но **не начинаться** с них.
- Может содержать **подчёркивание `_`**.

### Идентификатор в Python НЕ МОЖЕТ:

- Не может содержать **пробелы, спецсимволы** (`-`, `!`, `@`, и т.д.).
- Не может быть **пустой строкой**.
- Не может совпадать с **ключевым словом Python** (например, `for`, `class`, `def`).

---

#### Примеры `isidentifier()`

```python
"var".isidentifier()        # True  
"var_1".isidentifier()      # True  
"_temp".isidentifier()      # True  
"привет".isidentifier()     # True (кириллица тоже допустима)

"1var".isidentifier()       # False (начинается с цифры)
"my-var".isidentifier()     # False (минус запрещён)
"hello world".isidentifier()# False (пробелы запрещены)
"".isidentifier()           # False (пустая строка)
```

⚠️ Важно: `isidentifier()` **не проверяет ключевые слова**.
Например:

```python
"for".isidentifier()   # True ✅
```

Хотя в коде `for` нельзя использовать как имя переменной.
Для проверки на **ключевое слово** используют модуль `keyword`:

```python
import keyword
keyword.iskeyword("for")   # True
```



