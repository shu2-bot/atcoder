lst = []

for i in range(5):
    num = int(input())
    lst.append(num)

k = int(input())

b = 1
for a in lst:
    if k < a-lst[0]:
        print(":(")
        break
    b += 1

if b == 6:
    print("Yay!")