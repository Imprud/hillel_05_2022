def foo(*args):
    return "kaka"


class Person:
    def get_name(*args):
        return "Dima"


dima = Person
print(dima.get_name())

print(Person.get_name())
