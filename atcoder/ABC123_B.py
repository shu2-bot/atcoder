max = 0
val = 0
dis = 0
lst = []
valdis = 0

for i in range(5):
    num = int(input())
    val = 0
    while num > val:
        val += 10

    dispre = val - num

    if dis < dispre:
        dis = dispre
        max = num
        lst.append(valdis)
        valdis = val
    else:
        lst.append(val)

print(sum(lst) + max)