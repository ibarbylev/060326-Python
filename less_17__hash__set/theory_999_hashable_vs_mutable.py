# --- Не изменяемый, но не хэшируемый ---------------

t = (1, 2, [3])

try:
    hash(t)
except TypeError as e:
    print(e)


# --- Хэшируемый, но изменяемый --------------------

class Hashable:
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return 777


h = Hashable(1)
print(h.x)      # 1
print(hash(h))  # 777

h.x = 2
print(h.x)      # 2
print(hash(h))  # 777


"""
Python гарантирует не “абсолютную неизменяемость”, а стабильность хэша и поведения.

В Python hashable ВСЕГО ЛИШЬ означает, 
что объект ведёт себя как неизменяемый в части, влияющей на hash.
"""