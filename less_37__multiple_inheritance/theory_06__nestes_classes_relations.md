## Вложенные классы: ключевая идея

Вложенные классы **не создают автоматически связи** 
* ни между классами, 
* ни между экземплярами.  

Они ТОЛЬКО создают пространство имён: `i = Outer.Inner()`

Все связи между объектами могут быть созданы ТОЛЬКО ЯВНО, так как:
* `Outer` не получает объект `Inner` по умолчанию;
* `Inner` не получает доступ к экземплярам `Outer` по умолчанию.

Предел "автоматического возможного":
* Доступ к атрибуту самого класса `Outer` (не не его экземпляров!) из методов класса `Inner`.

```python
class Outer:
    class_attr = 100   # атрибут КЛАССА

    class Inner:
        def show_outer_class_attr(self):
            print(Outer.class_attr)   # ✔ доступ есть

i = Outer.Inner()
i.show_outer_class_attr()
```

---

### Пример 1. Нет связи ни между классами, ни между объектами*

```python
class Human:
    class Heart:
        def beat(self):
            return "Тук-тук"

# Создаём отдельные объекты
some_human = Human()
heart = Human.Heart()

# Попытка узнать "чьё это сердце" со стороны человека (some_human):
try:
    print(some_human.heart.beat())
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")  
    # AttributeError: 'Human' object has no attribute 'heart'

# Попытка узнать "что это за человек" со стороны сердца (heart):
try:
    print(heart.Human())
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
    # AttributeError: 'Heart' object has no attribute 'Human
```

**Вывод:**

* `Heart` существует как класс внутри `Human`.
* **Нет связи между объектом `alice` и объектом `heart`**, если мы её явно не создаём.

---

### Пример 2. Связь Алисы и сердца через явное создание атрибута

```python
class Human:
    def __init__(self, name):
        self.name = name
        self.heart = self.Heart()  # Явная связь с экземпляром

    class Heart:
        def beat(self):
            return "Тук-тук"

# У Алисы появилось сердце (можно вызвать его биение через dot-notation)
alice = Human("Alice")
print(alice.heart.beat())    # Тук-тук

# Но по-прежнему невозможно найти хозяина по сердцу
heart = alice.Heart()
try:
    print(heart.name)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")  
    # AttributeError: 'Heart' object has no attribute 'name'
```

**Вывод:**

* Экземпляр `Heart` **связан с конкретным экземпляром `Human`** через `self.heart = self.Heart(self).
* Связь создаётся **явно**, через конструктор.
* Обратной связи (сердце-человек) по-прежнему нет

---

### Пример 3. Взаимная связь между Human и Heart

Теперь можно сделать так, чтобы **человек знал своё сердце, а сердце знало человека** (двусторонняя связь):

```python
from __future__ import annotations

class Human:
    def __init__(self, name):
        self.name = name
        self.heart: Human.Heart = self.Heart(self)  # Связь с объектом Heart

    class Heart:
        def __init__(self, owner: Human):
            self.owner = owner  # сердце знает человека

        def beat(self):
            return "Тук-тук"

        def whose_heart(self):
            return f"Это сердце {self.owner.name}"

        def person_name(self):
            return self.owner.name

alice = Human("Alice")
print(alice.heart.beat())           # Тук-тук
print(alice.heart.whose_heart())    # Это сердце Alice
print(alice.heart.person_name())    # Alice

# Можно ещё создать Bob
bob = Human("Bob")
print(bob.heart.whose_heart())      # Это сердце Bob
```

**Вывод:**

* Мы создали **двустороннюю связь**, но она всё равно **явная**: вложенный класс не создаёт её автоматически.
* Вложенность служит **только для логической группировки и удобного пространства имён**.

---

### Итоговая концепция:

| Пример | Связь классов | Связь объектов          | Комментарий                                      |
| ------ | ------------- | ----------------------- | ------------------------------------------------ |
| 1      | Нет           | Нет                     | Только пространство имён                         |
| 2      | Нет           | Есть (человек → сердце) | Связь создана явно через атрибут                 |
| 3      | Нет           | Есть двусторонняя       | Связь создана явно через атрибуты обоих объектов |

