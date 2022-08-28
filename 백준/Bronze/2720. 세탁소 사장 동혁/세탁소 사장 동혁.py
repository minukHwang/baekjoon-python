n = int(input())
coin = [25, 10, 5, 1]

for i in range(n):
    change = []
    money = int(input())
    for item in coin:
        change.append(money//item)
        money = money % item
    for item in change:
        print(item, end = " ")
    print()

