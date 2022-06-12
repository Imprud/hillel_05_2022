import sys
from random import choice
from string import ascii_letters

# data = ["Dima", "Tanya", ...]


def get_random_string(n: int) -> str:
    return "".join(choice(ascii_letters) for _ in range(n))


data = [get_random_string(100) for _ in range(100_000)]
enum_data = enumerate(data)


dict_from_enum = {k: v for k, v in enum_data}
gener = (d for d in data)


print("List size: ", sys.getsizeof(data))
print("Enum list size: ", sys.getsizeof(enum_data))
print("Dict from enum data size: ", sys.getsizeof(dict_from_enum))
print("gener elements ", sys.getsizeof([i for i in gener]))
