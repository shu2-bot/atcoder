S = input()
T = input()

word = ['a','t','c','o','d','e','r']

ans = 0

for Sn, Tn in zip(S, T):
    if Sn != Tn:
        if Sn == '@':
            if Tn not in word:
                print('You will lose')
                ans = 1
                break
        elif Tn == '@':
            if Sn not in word:
                print('You will lose')
                ans = 1
                break
        else:
            print('You will lose')
            ans = 1
            break

if ans == 0:
    print('You can win')