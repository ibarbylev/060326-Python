### 5. DIP: Dependency Inversion Principle (принцип инверсии зависимостей)

***Модули верхнего уровня не должны зависеть от модулей нижнего уровня.  
Оба типа должны зависеть от абстракций (интерфейсов или базовых классов).  
Абстракции не должны зависеть от деталей, а детали должны зависеть от абстракций.***

Это делает систему гибкой: можно легко менять конкретные реализации без изменения кода, который их использует.

Согласно Роберту Мартину (автору SOLID):
* **Высокоуровневый модуль** — содержит важную политику и бизнес-правила. 
  * Он отвечает на вопрос «что должна делать система».

* **Низкоуровневый модуль** — содержит детали реализации. 
  *  Он отвечает на вопрос «как именно это делается».
---

### **Пример на Python**

**Нарушение DIP:**

```python
class UserService:          # ← высокоуровневый модуль
    def __init__(self):
        self.db = MySQLDatabase()  # зависимость от конкретной реализации
        
    def save_user(self, user):
        self.db.save(user)  # бизнес-операция «сохранить пользователя»

        
class MySQLDatabase:        # ← низкоуровневый модуль
    def save(self, data):
        print(f"Saving {data} to MySQL database")  # конкретная техническая деталь
```

Проблема: 
* `UserService` жестко зависит от `MySQLDatabase`.   
* Если захотим сменить базу на PostgreSQL, придётся менять сам класс `UserService`.

---

### Реализация DIP с помощью абстракции и внедрения зависимостей (Dependency Injection):

```python
from abc import ABC, abstractmethod

# Абстракция
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

# Конкретные реализации
class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL database")

# Класс верхнего уровня зависит от абстракции
class UserService:
    def __init__(self, db: Database):
        self.db = db

    def save_user(self, user):
        self.db.save(user)

        
mysql_service = UserService(MySQLDatabase())
mysql_service.save_user("Alice")  # Saving Alice to MySQL database

postgres_service = UserService(PostgreSQLDatabase())
postgres_service.save_user("Bob")  # Saving Bob to PostgreSQL database
```

* Теперь `UserService` **не зависит от конкретной базы**, а только от интерфейса `Database`. 
* Любую реализацию можно подставлять без изменения логики верхнего уровня — это и есть DIP.

---

Базовый (некорректный) пример — **композиция**.  
Исправленный вариант — пример **агрегации**.

Из этого примера можно сделать ошибочный вывод: "композиция всегда нарушает принцип DIP".

Это не верно: вот пример композиции, которая не нарушает DIP.

```python
from dataclasses import dataclass, field
from typing import List
from decimal import Decimal


@dataclass
class OrderItem:
    product_name: str
    quantity: int
    unit_price: Decimal

    def line_total(self) -> Decimal:
        return self.unit_price * self.quantity

    
@dataclass
class Order:
    customer_id: str
    _items: List[OrderItem] = field(default_factory=list, init=False)

    def add_item(self, product_name: str, quantity: int, unit_price: Decimal) -> None:
        # Классическая композиция: Order сам создаёт и полностью владеет OrderItem
        item = OrderItem(product_name, quantity, unit_price)
        self._items.append(item)

    def total(self) -> Decimal:
        return sum(item.line_total() for item in self._items)
```

В этом примере и `OrderItem`, и `Order` относятся к одной предметной области (доменной модели).  
Иными словами, оба класса описывают сам бизнес-процесс, а не способ его реализации.  
`OrderItem` **НЕ** является инфраструктурной деталью реализации (как БД для записи данных),  
а представляет собой часть сущности заказа `Order`.  
Поэтому композиция здесь естественна и не ведёт к нарушению DIP или иного принципа SOLID.