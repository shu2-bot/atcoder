H, W = map(int,input().split())
h, w = map(int,input().split())

val = H * (W - w)
dis = h*(W-w)
val = val - dis
print(val)