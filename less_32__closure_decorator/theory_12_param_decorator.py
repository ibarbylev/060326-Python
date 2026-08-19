"""
parameterized decorator (параметризированный декоратор)
или декоратор c параметрами
"""


from functools import wraps


def param_decorator(parameter):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Wrapper's doc_string"""
            print(50 * '*')
            result = func(*args, **kwargs)
            print(50 * '*')
            return parameter * f"<{result}>"
        return wrapper
    return decorator


@param_decorator(2)
def some_func(comment):
    """Doc_string for some_func"""
    print(f'Something useful...{comment}')
    print(f"The name of our function is ...{some_func.__name__}")
    print(f"The doc_string of our function is ...{some_func.__name__}")
    return 'RETURN FROM some_func _'


print(some_func('for me'))

# **************************************************
# Something useful...
# **************************************************
