import requests

NBU_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"


class CurrencyConverter:

    def __init__(self):
        self.rate = None
        self.date = None
        self.load_rate()

    def load_rate(self):
        response = requests.get(NBU_URL, timeout=10)
        response.raise_for_status()
        data = response.json()[0]
        self.rate = float(data["rate"])
        self.date = data["exchangedate"]

    def uah_to_usd(self, amount):
        return amount / self.rate


def main():
    try:
        converter = CurrencyConverter()
    except requests.RequestException as e:
        print(f"Could not get the exchange rate: {e}")
        return

    print(f"NBU rate on {converter.date}: 1 USD = {converter.rate} UAH")

    try:
        amount = float(input("Enter the amount in UAH: ").replace(",", "."))
    except ValueError:
        print("Please enter a number.")
        return

    print(f"{amount:.2f} UAH = {converter.uah_to_usd(amount):.2f} USD")


if __name__ == "__main__":
    main()