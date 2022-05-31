N, K = map(int, input().split())

lst = []
def kakuritu(val, base):
    num = 1
    while base >= val:
        val = val * 2
        num = num / 2
    num2 = (1/N) * num
    lst.append(num2)

n = 1
while n <= N:
    kakuritu(n, K-1)
    n = n + 1
ans = sum(lst)
print(ans)