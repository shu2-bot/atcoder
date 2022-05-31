n = int(input())
ans = 0
lst = list(map(int, input().split()))

for i in lst:
    while i % 2 == 0 or i % 3 == 2:
        ans += 1
        i -= 1
print(ans)