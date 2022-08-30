a, b = map(int, input().split())
count = 1
number = []

while len(number) < b:
    for i in range(count):
        number.append(count)
    count += 1

number = number[a-1:b]
print(sum(number))