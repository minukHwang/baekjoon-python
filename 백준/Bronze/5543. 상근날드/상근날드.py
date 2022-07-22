burger = []
coke = []

for i in range(3):
    a = int(input())
    burger.append(a)

for i in range(2):
    b = int(input())
    coke.append(b)

print(min(burger)+min(coke)-50)