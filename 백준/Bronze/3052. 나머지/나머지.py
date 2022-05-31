a = list()
b = set()
sum = 0

for i in range(10):
  a.append(int(input()))

for item in a:
  b.add(item%42)

print(len(b))