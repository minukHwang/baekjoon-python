time = 0

for i in range(4):
    n = int(input())
    time += n

x = time // 60
y = time % 60

print(x)
print(y)