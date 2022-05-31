n, s, t = map(int,input().split())
w = int(input())
anslst = [w]
for i in range(n-1):
    val = int(input())
    anslst.append(anslst[-1] + val)
ans = 0
for i in anslst:
    if i >= s and i <= t:
        ans += 1
print(ans)