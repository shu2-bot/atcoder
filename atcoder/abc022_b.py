"""
ans = 0
lst = []
for i in range(int(input())):
    n = int(input())
    if n in lst:
        ans += 1
    else:
        lst.append(n)
print(lst)
print(ans)
"""
n = int(input())

ans = list(int(input()) for i in range(n))
print(len(ans) - len(set(ans)))