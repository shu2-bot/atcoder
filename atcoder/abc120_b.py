A,B,K = map(int,input().split())

lst = []

val = 1
while val != 101:
    if (A % val == 0) and (B % val == 0):
        lst.append(val)
    val += 1

print(lst[len(lst) - K])