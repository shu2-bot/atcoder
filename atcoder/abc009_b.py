lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
for i in range(len(lst)):
    if lst[0] != lst[i]:
        print(lst[i])
        break