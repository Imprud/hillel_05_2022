import random
from threading import Lock, Thread

lst = []
lock = Lock()


def rund_list() -> None:
    global lst
    with lock:
        print(len(lst))
        for i in range(1000000):
            lst.append(random.randint(1, 1000))
        print(len(lst))
    return lst


def list_sum(lst: list[int]) -> None:
    with lock:
        return sum(lst)


def list_avarage(lst: list[int]) -> None:
    with lock:
        return sum(lst) / len(lst)


t1 = Thread(target=rund_list)
t2 = Thread(target=list_sum, args=(lst,))
t3 = Thread(target=list_avarage, args=(lst,))

t1.start()
t2.start()
t3.start()
t1.join()  # сказали сделать через лок thread lock
t2.join()
t3.join()
