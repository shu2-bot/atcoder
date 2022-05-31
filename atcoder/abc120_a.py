A,B,C = map(int,input().split())

c = 0
while B >= A:
    B = B - A
    if c == C:
        break
    c += 1

print(c)