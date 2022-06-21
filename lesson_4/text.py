def decor(func):
    def inner(*args, **kwargs):
        a = args[0]
        print(f"a = {a}")
        return func(*args, **kwargs)

    return inner


@decor
def test(a, b, c):
    return f"{a}, {b}, {c}"


print(test(1, 3, 4))
