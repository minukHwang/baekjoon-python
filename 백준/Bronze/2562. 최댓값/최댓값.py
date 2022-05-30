a = list()

for i in range(9):
    item = int(input())
    a.append(item)

m = max(a)
print(m)
print(a.index(m)+1)