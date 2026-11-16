result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b



data = [(10, 2), (2, 5), ("123", 4), (18, 0), ([], 15), (8, 4), (500, 150)]

for key, value in data:
    try:
        res = divider(key, value)
        result.append(res)
    except Exception as a:
        print(f"divider({key!r}, {value!r}) -> {type(a).__name__}: {a}")

print(result)