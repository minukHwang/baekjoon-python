import math
a, b, c = map(int, input().split())

bp = c - b

if bp <= 0:
    bp = -1
else:
    bp = a // bp + 1

    

print(bp)
            