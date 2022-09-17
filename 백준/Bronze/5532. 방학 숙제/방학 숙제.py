import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

kh = math.ceil(a/c)
mh = math.ceil(b/d)

print(l-max(kh,mh))