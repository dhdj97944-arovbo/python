try:
    print("start")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError):
    print("we have an error")


print("code after capsule")