num = set(range(1,10001))
b = set()

def not_self_num(a) :
    c = str(a)
    n = 0
    for i in c:
        n += int(i)
    n += a
    return n
    
for i in range(1, 10001):
    b.add(not_self_num(i))

self_num = num.difference(b)
self_num = list(self_num)
self_num.sort()

for i in self_num:
    print(i)