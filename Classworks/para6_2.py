try:
    print("start")
    print(10/0)
    print("no error")
except NameError:
    print("we have an error")
except ZeroDivisionError:
    print("we have an zero error")

print("code after capsule")