a = int(input())
b = int(input())
num = 0
if a < b:
    val = b - a
    if val > 5:
        num = val - 5
        val = 5 - num
else:
    val = a - b
    if val > 5:
        num = val - 5
        val = 5 - num
print(val)