"""
Итератор сам по себе является НЕИЗМЕНЯЕМЫМ.

НО!
Никто не запрещает нам изменять объект, на который он ссылается.
"""

lst = [1, 2, 3]

for i, value in enumerate(lst):
    print(i, value)
    lst.append(i)


"""
Изменять объект по которому итерируешь == пилить сук, на котором сидишь)

Решение проблемы:
"""


for i, value in enumerate(lst[:]):  # или lst.copy()
    print(i, value)
    lst.append(i)