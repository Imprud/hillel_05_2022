import random
from threading import Thread
from time import sleep

lst = []


def rund_list() -> list[int]:
    global lst
    for i in range(1000000):
        lst.append(random.randint(1, 1000))
    print(len(lst))
    return lst


def list_sum(lst: list[int]) -> int:
    print(sum(lst))
    return sum(lst)


def list_avarage(lst: list[int]) -> float:
    print(sum(lst) / len(lst))
    return sum(lst) / len(lst)


def main():
    t1 = Thread(target=rund_list)
    t2 = Thread(target=list_avarage, args=(lst,))
    t3 = Thread(target=list_sum, args=(lst,))

    t1.start()
    while t1.is_alive():
        sleep(0.2)
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
