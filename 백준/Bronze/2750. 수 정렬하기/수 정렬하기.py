n = int(input())
number = list()

for i in range(n):
    number.append(int(input()))

number.sort()

for item in number:
    print(item)