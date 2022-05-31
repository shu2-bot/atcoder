r, d, r2000 = map(int, input().split())

for i in range(1, 11):
    print(r * r2000 - d)
    r2000 = r * r2000 - d