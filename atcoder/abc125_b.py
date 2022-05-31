n = int(input())
val = []
for i in map(int, input().split()):
    val.append(i)
cost = []
for i in map(int, input().split()):
    cost.append(i)

ans = 0
for i in range(n):
    m = val[i] - cost[i]
    if m > 0:
        ans += m

print(ans)