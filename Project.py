import random
import sqlite3

import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"
DEFAULT_COINS = {"BTC": 90000.0, "ETH": 3000.0, "SOL": 150.0, "DOGE": 0.2}


def get_prices():
    prices = {}
    try:
        html = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}).text
        soup = BeautifulSoup(html, "html.parser")
        for row in soup.select("tbody tr"):
            symbol = row.select_one("p.coin-item-symbol")
            price = row.find(string=lambda t: t.startswith("$"))
            if symbol and price:
                prices[symbol.text.strip()] = float(price[1:].replace(",", ""))
    except Exception:
        pass
    if "BTC" not in prices:
        print("Не вдалося завантажити ціни. Беру запасні.")
        return DEFAULT_COINS
    return prices


def menu(conn):
    while True:
        print("\n1 - список монет")
        print("2 - ціна монети")
        print("3 - далі")
        choice = input("Вибір: ")
        if choice == "1":
            for symbol, price in conn.execute("SELECT symbol, price FROM coins"):
                print(symbol, "- $" + str(price))
        elif choice == "2":
            symbol = input("Символ монети: ").upper()
            row = conn.execute("SELECT price FROM coins WHERE symbol = ?", (symbol,)).fetchone()  # шукаю одну монету в базі
            if row:
                print(symbol, "- $" + str(row[0]))
            else:
                print("Такої монети немає")
        elif choice == "3":
            break


class Trader:  # клас нашого трейдера

    def __init__(self, name, price):
        self.name = name  # self - це сам трейдер
        self.price = price
        self.money = 5000
        self.coins = 0
        self.age = 25
        self.gladness = 50
        self.family = 50
        self.house = False
        self.kids = 0
        self.alive = True

    def capital(self):
        return self.money + self.coins * self.price

    def to_buy(self):
        print("Купую крипту")
        if self.money > 100:
            spend = self.money * 0.3
            self.coins += spend / self.price
            self.money -= spend

    def to_sell(self):
        print("Продаю крипту")
        self.money += self.coins * self.price
        self.coins = 0

    def to_family(self):
        print("Час із родиною")
        self.family += 8
        self.gladness += 4

    def to_sleep(self):
        print("Сплю")
        self.gladness += 3

    def to_chill(self):
        print("Відпочинок")
        self.gladness += 5
        self.family -= 2

    def die_of_old_age(self):
        print("Помер від старості")
        self.alive = False

    def is_alive(self):
        if self.money < 0 and self.coins <= 0:
            print("Банкрут")
            self.alive = False
        elif self.gladness <= 0:
            print("Депресія")
            self.alive = False
        elif self.family <= 0:
            print("Дружина пішла")
            self.alive = False
        elif self.age >= 90 or (self.age >= 70 and random.randint(1, 10) == 1):  # після 70 шанс 1 з 10
            self.die_of_old_age()

    def end_of_year(self):
        print(f"Курс = ${round(self.price, 2)}")
        print(f"Гроші = ${round(self.money, 2)} | Капітал = ${round(self.capital(), 2)}")
        print(f"Настрій = {self.gladness} | Сім'я = {self.family}")
        print(f"Будинок: {'є' if self.house else 'немає'} | Дітей: {self.kids}")

    def live(self, year):
        print(f"\nРік {year} життя {self.name}, вік {self.age}")
        self.price *= random.uniform(0.7, 1.4)
        live_cube = random.randint(1, 5)  # кубик - яку дію робити
        if live_cube == 1:
            self.to_buy()
        elif live_cube == 2:
            self.to_sell()
        elif live_cube == 3:
            self.to_family()
        elif live_cube == 4:
            self.to_sleep()
        elif live_cube == 5:
            self.to_chill()

        self.money += 8000
        self.money -= 2000 + self.kids * 1000
        if self.house:
            self.money -= 1000
        print("Заробіток і витрати за рік")

        if not self.house and self.money >= 15000:
            self.house = True
            self.money -= 10000
            print("Купив будинок!")
        if self.house and self.family > 60 and self.kids < 3 and random.randint(1, 6) == 1:
            self.kids += 1
            print("Народилася дитина!")
        self.end_of_year()
        self.age += 1
        self.is_alive()


conn = sqlite3.connect("crypto.db")
conn.execute("DROP TABLE IF EXISTS coins")
conn.execute("CREATE TABLE coins (symbol TEXT PRIMARY KEY, price REAL)")
prices = get_prices()
for symbol, price in prices.items():
    conn.execute("INSERT OR REPLACE INTO coins VALUES (?, ?)", (symbol, price))
conn.commit()  # зберігаю зміни

menu(conn)

trader = Trader("Алекс", prices["BTC"])

for year in range(100):
    if trader.alive == False:
        break
    trader.live(year)

print("\nСимуляція закінчена!")
menu(conn)
conn.close()