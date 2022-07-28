n, k = map(int, input().split())
coins = []
amount = 0

for i in range(n):
    coin = int(input())
    if coin > k:
        continue
    else:
        coins.insert(0,coin)

for item in coins:
    if k//item > 0 :
        amount += k//item
        k -= (k//item) * item
    else:
        continue

print(amount)