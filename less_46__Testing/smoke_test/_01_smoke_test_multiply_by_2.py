"""
Module with function multiply_by_2 and its tests
"""


def multiply_by_2(num: int) -> int | str:
    """
    Function returns integer <num> multiplied by 2.
    """

    if isinstance(num, int):
        return 2 * num
    return 'Error!!! Argument <num> must be integer!!!'


if __name__ == "__main__":
    if not multiply_by_2(2) == 4:
        print('Correct multiply positive is not true!')

    if not multiply_by_2(2) == 4:
        print('Correct multiply positive is not true!')

    if not multiply_by_2(-2) == -4:
        print('Correct multiply negative is not true!')

    if not multiply_by_2(2) != 5:
        print('Incorrect multiply positive is not true!')

    if not multiply_by_2(-2) != -5:
        print('Incorrect multiply negative is not true!')

    if not multiply_by_2(0) == 0:
        print('Multiply by zero is not equal zero!')

    if not multiply_by_2("str") == 'Error!!! Argument <num> must be integer!!!':
        print('Wrong answer if <num> is string!')

    if not multiply_by_2(0.1) == 'Error!!! Argument <num> must be integer!!!':
        print('Wrong answer if <num> is float!')



