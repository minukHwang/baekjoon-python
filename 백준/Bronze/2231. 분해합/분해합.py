n = int(input())
bunhae = []

for i in range(1,n):
    number = str(i)
    total = 0
    for item in number:
        total += int(item)
    total += i
    if total == n:
        bunhae.append(i)


if len(bunhae) ==0:
    print(0)
else:
    print(min(bunhae))