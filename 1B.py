def metro(total, start, end):
    dist1= abs(end - start) - 1
    dist2 = total - dist1 - 2
    return min(dist1, dist2)

n, i, j = map(int, input().split())
print(metro(n, i, j))