import sys
print("sys.path[0] до изменения:", sys.path[0])

# import os
# # Получаем абсолютный путь к текущему файлу
# current_file = os.path.abspath(__file__)
#
# # Поднимаемся на уровень выше (из test/ в корень проекта)
# project_root = os.path.dirname(os.path.dirname(current_file))
#
# # Добавляем корень проекта в начало sys.path
# sys.path.insert(0, project_root)
#
# print("sys.path[0] после изменения:", sys.path[0])

from library import greet1, greet2


greet1()
greet2()