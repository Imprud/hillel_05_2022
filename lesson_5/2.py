def rep(num):
    if all(
        (
            num > 0,
            num % 6 == 0,
            num % 8 == 0,
        )
    ):
        print(num)


rep(48)
