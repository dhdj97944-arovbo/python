import sqlite3

import requests

DB_NAME = "weather.db"

WEATHER_URL = ("https://api.open-meteo.com/v1/forecast"
               "?latitude=51.4982&longitude=31.2893&current=temperature_2m")


def create_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS weather (""date_time TEXT NOT NULL, ""temperature REAL NOT NULL)")


def get_temperature():
    response = requests.get(WEATHER_URL, timeout=10)
    response.raise_for_status()
    return float(response.json()["current"]["temperature_2m"])


def save_temperature(temperature):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO weather VALUES (datetime('now', 'localtime'), ?)",(temperature,))


def show_all():
    with sqlite3.connect(DB_NAME) as conn:
        for date_time, temperature in conn.execute("SELECT * FROM weather"):
            print(f"{date_time} // {temperature} C")


def main():
    create_db()
    try:
        temperature = get_temperature()
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Could not get the temperature: {e}")
        return
    save_temperature(temperature)
    print(f"Saved: Chernihiv, {temperature} C\n")
    print("Database content:")
    show_all()


if __name__ == "__main__":
    main()