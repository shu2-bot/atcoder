N,M,C = map(int,input().split())

B = list(map(int,input().split()))

ans = 0
for i in range(N):
    val = 0
    A = list(map(int,input().split()))
    for i in range(M):
        val += A[i-1]*B[i-1]
    if val + C > 0:
        ans += 1

print(ans)