import random


class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0.0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Час вчитися.")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Піду посплю.")
        self.gladness += 3

    def to_chill(self):
        print("Час відпочивати (гроші витрачаються).")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 30

    def to_work(self):
        print("Іду на підробіток.")
        self.money += 50
        self.gladness -= 4

    def choose_action(self):
        if self.money < 30:
            print("(Грошей немає, потрібно працювати)")
            return self.to_work
        if self.progress < 0:
            print("(Проблеми з навчанням, треба вчитися)")
            return self.to_study
        if self.gladness < 30:
            print("(Настрій поганий, потрібен відпочинок)")
            return self.to_chill if self.money >= 60 else self.to_sleep
        return random.choice([self.to_study, self.to_sleep,self.to_chill, self.to_work])

    def check_state(self):
        self.gladness = min(self.gladness, 100)
        if self.progress < -0.5:
            print("Відрахований.")
            self.alive = False
        elif self.gladness <= 0:
            print("Депресія.")
            self.alive = False

    def end_of_day(self):
        print(f"Радість = {self.gladness}")
        print(f"Прогрес = {round(self.progress, 2)}")
        print(f"Гроші = {self.money}\n")

    def live(self, day):
        print(f"-=- День {day} життя {self.name} -=-")
        self.choose_action()()
        self.check_state()
        self.end_of_day()


if __name__ == "__main__":
    stud = Student(name="Василь")

    for day in range(1, 366):
        if not stud.alive:
            print(f"{stud.name} не дожив до кінця року (день {day - 1}).")
            break
        stud.live(day)
    else:
        print(f"{stud.name} успішно прожив рік! "
              f"Прогрес: {round(stud.progress, 2)}, гроші: {stud.money}.")
