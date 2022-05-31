
n = int(input())
a, b = map(int,input().split())
k = int(input())
road = (list(map(int,input().split())))

road2 = set(road)
if a in road or b in road:
    print('NO')
elif len(road2) != len(road):
    print('NO')
else:
    print('YES')