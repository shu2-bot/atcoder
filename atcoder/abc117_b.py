n = int(input())

lst = []
for i in map(int, input().split()):
    lst.append(i)

if max(lst) < sum(lst) - max(lst):
    print('Yes')
else:
    print('No')