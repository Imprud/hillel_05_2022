def get_primes_amount(num: int) -> int:
    results = 0
    for i in range(1, num + 1):
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        results += 1

    return results


numbers = [40000, 400, 10, 700]

for i in numbers:
    print(get_primes_amount(i))
    print(i)
