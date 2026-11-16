import random

brand_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 8},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 6},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 10},
}

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 30, "gladness_less": 5},
    "C++ developer": {"salary": 60, "gladness_less": 20},
    "Rust developer": {"salary": 70, "gladness_less": 15},
}


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        print("The car can't move")
        return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


class Pet:

    def __init__(self, name, kind="cat"):
        self.name = name
        self.kind = kind
        self.hunger = 30   # 0 - full, 100 - very hungry
        self.mood = 60     # 0 - sad, 100 - happy

    def eat(self):
        self.hunger = max(0, self.hunger - 30)
        self.mood = min(100, self.mood + 5)

    def play(self):
        self.mood = min(100, self.mood + 20)
        self.hunger = min(100, self.hunger + 5)

    def new_day(self):
        self.hunger = min(100, self.hunger + 10)
        self.mood = max(0, self.mood - 3)
        if self.hunger > 80:
            self.mood = max(0, self.mood - 10)

    def joy_for_owner(self):
        return 3 if self.mood >= 50 else -3


class Human:
    def __init__(self, name="human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car
        self.pet = pet

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_pet(self):
        self.pet = Pet("Whiskers")

    def get_job(self):
        if self.can_drive():
            self.job = Job(job_list)

    def can_drive(self):
        if self.car.fuel < self.car.consumption:
            print("Refueling the car")
            self.money -= 100
            self.car.fuel += 100
        if self.car.strength <= 0:
            self.to_repair()
        return self.car.drive()

    def to_repair(self):
        print("Repairing the car")
        self.car.strength += 100
        self.money -= 50

    def eat(self):
        if self.home.food < 10:
            self.shopping("food")
        else:
            self.satiety = min(100, self.satiety + 20)
            self.home.food -= 10

    def work(self):
        if not self.can_drive():
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 1

    def shopping(self, manage):
        if not self.can_drive():
            return
        if manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "treats":
            print("Very delicious")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 15
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def feed_pet(self):
        if self.home.food < 10:
            print("No food for the pet, going shopping")
            self.shopping("food")
        else:
            print(f"Feeding the pet {self.pet.name}")
            self.home.food -= 10
            self.pet.eat()

    def play_with_pet(self):
        print(f"Playing with {self.pet.name}")
        self.pet.play()
        self.gladness += 5

    def days_indexes(self, day):
        print(f"{'Day ' + str(day) + ' of ' + self.name + chr(39) + 's life':=^50}")
        print(f"{self.name}: money - {self.money}, satiety - {self.satiety}, "
              f"gladness - {self.gladness}")
        print(f"Home: food - {self.home.food}, mess - {self.home.mess}")
        print(f"{self.car.brand} car: fuel - {self.car.fuel}, "
              f"strength - {self.car.strength}")
        print(f"Pet {self.pet.name}: hunger - {self.pet.hunger}, "
              f"mood - {self.pet.mood}")

    def is_alive(self):
        if self.gladness <= 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Died of hunger...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    def end_of_day(self):
        self.satiety -= 3
        self.gladness -= 1
        self.pet.new_day()
        self.gladness += self.pet.joy_for_owner()

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print("Settled in the home")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Bought a car {self.car.brand}")
        if self.pet is None:
            self.get_pet()
            print(f"Got a pet {self.pet.name}")
        if self.job is None:
            self.get_job()
            if self.job:
                print(f"Got a job: {self.job.job}, salary {self.job.salary}")
        self.days_indexes(day)

        dice = random.randint(1, 5)
        if self.satiety < 30:
            print("I'll go eat")
            self.eat()
        elif self.pet.hunger > 60:
            self.feed_pet()
        elif self.gladness < self.job.gladness_less + 20:
            if self.home.mess > 15:
                print("I want to chill, but there is too much mess. I will clean.")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money < 100:
            print("Time to work")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Time to work")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping("treats")
        else:
            self.play_with_pet()

        self.end_of_day()
        return self.is_alive()


if __name__ == "__main__":
    test_human = Human(name="Vasya")

    for day in range(1, 31):
        if test_human.live(day) is False:
            break