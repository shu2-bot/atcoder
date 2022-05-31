import random

n = int(input())
def kouyakusuu(lst):
    m = lst[0]
    while lst[1] % m != 0:
        m -= 1
    for i in range(2,len(lst)):
        while lst[i] % m != 0:
            m -= 1
    return m

a = []
for i in map(int, input().split()):
    a.append(i)



ans = kouyakusuu(a)
print(ans)