class Countdown:

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


countdown = Countdown(5891952) # впадлу було робити маленьке число

print("Type of object      :", type(countdown).__name__)
print("Type of iter(object):", type(iter(countdown)).__name__)

print("First pass :", [x for x in countdown])
print("Second pass:", [x for x in countdown])

for number in countdown:
    print(number)