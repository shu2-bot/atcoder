N,M = map(int,input().split())

lst = []

for i in range(N):
    val = tuple(map(int,input().split()))
    lst.append(val)

A = []
for i in range(N):
    A.append(lst[i-1][0])

val = 0
while M > 0:
    res = A.index(min(A))
    if M - lst[res][1] > 0:
        val += lst[res][0]*lst[res][1]
        M = M - lst[res][1]
        lst.pop(res)
    else:
        val += lst[res][0]*M
        break

print(val)