### Почему Student не считает свои объекты?

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        self.__class__.population += 1

    @classmethod
    def get_population(cls):
        return cls.population


class Student(Person):
    pass


p1 = Person("John")
print(id(Student.population) == id(Person.population))
print("Student: ", Student.population, "Person", Person.population)

p2 = Person("Mary")
print(id(Student.population) == id(Person.population))
print("Student: ", Student.population, "Person", Person.population)

s1 = Student("Peter")
print(id(Student.population) == id(Person.population))
print("Student: ", Student.population, "Person", Person.population)


# True
# Student:  1 Person 1
# True
# Student:  2 Person 2
# False
# Student:  3 Person 2
```

## Пояснения

Атрибуты классов не копируются при наследовании.  
Они ищутся через MRO (цепочку наследования).  

Пока у дочернего класса `Student` нет собственного атрибута `population`,   
обращение к `Student.population` находит атрибут в родительском классе `Person`.

Но как только создаётся первый экземпляр дочернего класса, операция присваивания 
```python
self.__class__.population += 1
``` 
тут же создаёт новый атрибут класса `population` именно в дочернем классе `Student`.