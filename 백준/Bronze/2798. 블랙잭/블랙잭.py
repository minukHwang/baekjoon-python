n, m = map(int, input().split())
cards = list(map(int, input().split()))
yes = list()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] <= m:
                yes.append(cards[i] + cards[j] + cards[k])

print(max(yes))