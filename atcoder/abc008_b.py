n = int(input())

namelst = []
namecnt = []
for i in range(n):
    namelst.append(input())
for i in range(n):
    namecnt.append(namelst.count(namelst[i]))
print(namelst[namecnt.index(max(namecnt))])