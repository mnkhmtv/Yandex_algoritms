def date(x, y):
    if x == y:
        return 1
    elif x <= 12 and y <= 12:
        return 0
    return 1
x, y, z, = map(int, input().split())
print(date(x, y))