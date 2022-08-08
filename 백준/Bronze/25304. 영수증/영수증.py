total = int(input())
count = int(input())
compare = 0

for i in range(count):
    cash, amount = map(int, input().split())
    compare += cash * amount

if compare == total:
    print("Yes")
else:
    print("No")