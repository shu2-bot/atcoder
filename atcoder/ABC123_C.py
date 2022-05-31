'''
num = int(input())

lst = []
pos = [0,0,0,0,0]

for i in range(5):
    lst.append(i)

pos[0] = num
while (pos[0] + pos[1] + pos[2] + pos[3]) != 0:
    if pos[0] != 0:
        if pos[0] >= lst[0]:
            pos[1] += lst[0]
        else:
            pos[1] += pos[0]
    
    if pos[1] != 0:
        if pos[1] >= lst[1]:
            pos[2] += lst[1]
        else:
            pos[2] += pos[1]
    
    if pos[2] != 0:
        if pos[2] >= lst[2]:
            pos[3] += lst[2]
        else:
            pos[3] += pos[2]

    if pos[3] != 0:
        if pos[3] >= lst[3]:
            pos[4] += lst[3]
        else:
            pos[4] += pos[3]
    
print(pos,lst)
'''
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
 
min = min(A, B, C, D, E)
 
ans = 4 + int(N/min)
if N % min != 0:
    ans = ans + 1
print(ans)
