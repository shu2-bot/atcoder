num = 0
a, b = map(int, input().split())

num = a
a = b
b = num

print(str(a) + ' ' + str(b))