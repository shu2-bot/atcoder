s = list(input())

ans = 0
key_lst =  ['A', 'T', 'C', 'G']
ans_lst = []

for i in s:
    if i in key_lst:
        ans += 1
    else:
        ans_lst.append(ans)
        ans = 0

print(max(ans_lst))