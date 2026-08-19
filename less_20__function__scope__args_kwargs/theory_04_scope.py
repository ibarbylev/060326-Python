count = 0


def outer():
    count = 1
    print("inside the outer function before the inner function", count, id(count))

    def inner():
        count = 2
        print("inside the inner function", count, id(count))

    inner()
    print("inside the outer function after the inner function", count, id(count))


print("before the outer function", count, id(count))
outer()
print("after the outer function", count, id(count))
