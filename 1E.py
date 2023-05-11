d = int(input())
x, y = map(int, input().split())
def f(x, y, d):
    r = [
    [x ** 2 + y ** 2, 1],
    [(x - d) ** 2 + y ** 2, 2],
    [x ** 2 + (y - d) ** 2, 3]
    ]

    if (y <= d - x and 0 <= x <= d and 0 <= y <= d):
        return 0 
    
    return min(r)[1]

print(f(x, y, d))