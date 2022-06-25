from currency_rate import CurrencyProcessor


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __add__(self, other):

        if self.currency != other.currency:
            other.amount = CurrencyProcessor.convert_cur_to_cur(
                from_currency=other.currency,
                to_currency=self.currency,
                amount=other.amount,
            )
        return Price(self.amount + other.amount, self.currency)

    def __sub__(self, other):

        if self.currency != other.currency:
            other.amount = CurrencyProcessor.convert_cur_to_cur(
                from_currency=other.currency,
                to_currency=self.currency,
                amount=other.amount,
            )
        return Price(self.amount - other.amount, self.currency)


def main():
    p1 = Price(100, "EUR")
    p2 = Price(3300, "UAH")
    p3 = p1 + p2
    print(p3.amount)
    # p4 = p1-p2
    # print(p4.amount)


if __name__ == "__main__":
    main()
