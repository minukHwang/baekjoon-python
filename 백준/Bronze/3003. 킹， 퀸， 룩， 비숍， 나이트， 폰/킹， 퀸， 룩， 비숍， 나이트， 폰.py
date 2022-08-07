chess = [1,1,2,2,2,8]

n = list(map(int, input().split()))

for i in range(6):
    difference = chess[i] - n[i]
    print(difference, end=" ")