### Пояснения к [./theory_01__tuple.md](theory_01__tuple.md)

```python
n1, n2, lst = 1, 2, [1, 2]

t = (n1, n2, lst)

print(t)         # (1, 2, [1, 2])
print(type(t))   # <class 'tuple'>

print(id(n1), id(n2), id(lst))       # 12216648 12216680 140492792400640
print(id(t[0]), id(t[1]), id(t[2]))  # 12216648 12216680 140492792400640

lst = [1, 2, 3]
print(lst)      # [1, 2, 3]
print(id(lst))  # 140492792400640

print(t)  # (1, 2, [1, 2, 3])
```