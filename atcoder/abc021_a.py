n = int(input())
ans = 0
anslst = []
while n >= 8:
    ans += 1
    n -= 8
    anslst.append(8)
while n >= 4:
    ans += 1
    n -= 4
    anslst.append(4)
while n >= 2:
    ans += 1
    n -= 2
    anslst.append(2)
if n != 0:
    ans += 1
    anslst.append(1)
print(ans)
for i in anslst:
    print(i)