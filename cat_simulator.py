import random


class Cat:


    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.mood = 50
        self.alive = True

    def feed(self):
        print(f"{self.name} поїв.")
        self.hunger -= 30
        self.mood += 5

    def play(self):
        print(f"{self.name} грається з клубком.")
        self.mood += 15
        self.hunger += 10

    def sleep(self):
        print(f"{self.name} спить")
        self.hunger += 5
        self.mood += 3

    def check(self):
        self.hunger = max(0, min(100, self.hunger))
        self.mood = min(100, self.mood)
        if self.hunger >= 100:
            print(f"{self.name} занадто голодний")
            self.alive = False
        elif self.mood <= 0:
            print(f"{self.name} пішов шукати новий дім")
            self.alive = False

    def live(self, day):
        print(f"-=- День {day} -=-")
        random.choice([self.feed, self.play, self.sleep])()
        self.mood -= 5  # котик сумує без уваги
        self.check()
        print(f"Голод: {self.hunger} // Настрій: {self.mood}\n")


if __name__ == "__main__":
    cat = Cat("Вася")
    for day in range(1, 94):
        if not cat.alive:
            break
        cat.live(day)