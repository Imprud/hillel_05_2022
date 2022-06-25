import json

from requests_html import HTMLSession

API_KEY = "5s2qhqxRR1iOs95qSYW14N2WHbNDBbGx"


class CurrencyProcessor:
    @staticmethod
    def get_currency_rate(
        from_cur: str, to_cur: str, amount: float | int
    ) -> float | None:
        with HTMLSession() as session:
            url = f"https://api.apilayer.com/fixer/convert?to={to_cur}&from={from_cur}&amount={amount}"
            # reps_json = json.loads(resp_text)
            # payload = {}
            headers = {"apikey": API_KEY}
            response = session.get(url, headers=headers)
            status_code = response.status_code
            if status_code == 200:
                result_json = json.loads(response.text)
                return result_json["result"]

    @classmethod
    def convert_to_USD(cls, currency: str, amount: int | float):
        if currency != "USD":
            amount = cls.get_currency_rate(
                from_cur=currency, to_cur="USD", amount=amount
            )
        return amount

    @classmethod
    def convert_cur_to_cur(
        cls, from_currency: str, to_currency: str, amount: float | int
    ):
        usd_amount = cls.convert_to_USD(from_currency, amount)
        if to_currency != "USD":
            converted_currency_amount = cls.get_currency_rate(
                from_cur="USD", to_cur=to_currency, amount=usd_amount
            )
            return converted_currency_amount
        return usd_amount
