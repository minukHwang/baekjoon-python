t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    b = []
    for j in range(7):
        if a[j] % 2 == 0:
            b.append(a[j])
    print(sum(b), min(b))
            