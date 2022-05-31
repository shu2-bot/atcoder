n = int(input())

val1 = str(n//3600)
if len(val1) == 1:
    val1 = '0' + val1
n = n%3600
val2 = str(n//60)
if len(val2) == 1:
    val2 = '0' + val2
n = str(n%60)
if len(n) == 1:
    n = '0' + n

print(val1 + ':' + val2 + ':' + n)