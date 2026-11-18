from timeit import repeat

import requests
from bs4 import BeautifulSoup

NBU_URL = "https://bank.gov.ua/ua/markets/exchangerates"


class CurrencyConverter:

    def __init__(self):
        self.rate = None
        self.date = "unknown"
        self.load_rate()

    def load_rate(self):
        response = requests.get(NBU_URL, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for row in soup.find_all("tr"):
            cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
            if "USD" not in cells:
                continue
            for cell in cells:
                if "." in cell or "," in cell:
                    try:
                        self.rate = float(cell.replace(",", "."))
                        break
                    except ValueError:
                        continue
            if self.rate:
                break

        if self.rate is None:
            raise ValueError("USD rate not found on the page")

        for word in soup.get_text().split():
            if len(word) == 10 and word[2] == "." and word[5] == ".":
                self.date = word
                break

    def uah_to_usd(self, amount):
        return amount / self.rate

    def usd_to_uah(self, amount):
        return amount * self.rate


def main():
    try:
        converter = CurrencyConverter()
    except (requests.RequestException, ValueError) as e:
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