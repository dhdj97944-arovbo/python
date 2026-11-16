try:
    try:
        print("start")
        print(vasya)
        print("no error")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)