class ExchangeRates:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        # if ExchangeRates._initialized is False:
        if hasattr(self, "message"):
            return
        else:
            self.message = "Hello from test"
            self.exchange_rates = []  # takes 10s

        # try:
        #     if self.message:
        #         return
        # except AttributeError:
        #     self.message = "Hello from test"
        #     self.exchange_rates = []  # takes 10s


er = ExchangeRates()
er2 = ExchangeRates()
er3 = ExchangeRates()

print(er)
print(er2)
print(er3)
