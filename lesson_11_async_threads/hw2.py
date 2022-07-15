import asyncio


async def get_primes_amount(num: int) -> int:
    results = 0
    for i in range(2, num + 1):
        await asyncio.sleep(0)
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if not flag:
            results += 1
    print(results)
    return results


async def main():
    numbers = [50000, 10000, 50, 100, 3]
    tasks = []
    for i in numbers:
        tasks.append(get_primes_amount(i))
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
