s = input()

if int(s[:2]) >= 13 or s[:2] == '00':
    if int(s[2:]) >= 13 or s[2:] == '00':
        print('NA')
    elif int(s[2:]) <= 12:
        print('YYMM')
else:
    if int(s[2:]) >= 13 or s[2:] == '00':
        print('MMYY')
    elif int(s[2:]) <= 12:
        print('AMBIGUOUS')