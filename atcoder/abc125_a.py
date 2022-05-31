a, b, t = map(int, input().split())

if a > t:
    print(0)
else:
    n = 1
    while (a * n) <= t:
        n += 1
    print(b * (n-1))