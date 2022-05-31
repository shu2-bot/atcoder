s = int(input())
N = input()
cnt = 0
n = 'b'

if len(N) == 1:
    if N == n:
        print(0)
    else:
        print(-1)

if len(N)>1:
    for i in range(1, (s-1)//2+1):
        if i%3==0:
            n = 'b' + n + 'b'
        if i%3==1:
            n = 'a' + n + 'c'
        if i%3==2:
            n = 'c' + n + 'a'
        cnt += 1
    
    if N == n:
        print(cnt)
    else:
        print(-1)