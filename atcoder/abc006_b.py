
n = int(input())

lst = [0, 0, 1]

while len(lst) < n:
    x = sum(lst)
    lst.append(x)
    lst.pop(0)
    n -= 1

print(lst[n-1]%10007)