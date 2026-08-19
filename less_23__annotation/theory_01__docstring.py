"""
Docstring - простой и удобный способ добавить детальное описание в функцию.
(что-то вроде инструкции пользователя.

Извлечь можно с помощью функции help().
"""


def my_function():
    """
    This is my function: very simple and very useful and very good way to add a description.
    Return nothing.

    :return: None
    """
    print("Hello World")


help(my_function)
help()

def f(x, y):
    """
    Adds two numbers and returns the result.

    This function takes two numerical inputs and adds them together. It
    is expected that both parameters are valid numbers that can be added.
    The result of the addition will be returned.

    :param x: The first number to be added.
    :type x: int or float
    :param y: The second number to be added.
    :type y: int or float
    :return: The sum of the two numbers.
    :rtype: int or float
    """