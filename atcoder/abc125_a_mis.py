a, b, t = map(float, input().split())

for n in range(20):
    if a > (t + 0.5):
        print(0)
        break
    elif a < (t + 0.5):
        if (a * n) > (t + 0.5):
            print(int(b * (n-1)))
            break
        if (a * n) < (t + 0.5):
            continue