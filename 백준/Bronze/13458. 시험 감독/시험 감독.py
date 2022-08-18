import math

n = int(input())
alist = list(map(int, input().split()))
b,c = map(int, input().split())
result = 0

for i in range(n):
    if alist[i] < b:
        result += 1
    else:
        result += math.ceil((alist[i] - b)/ c) + 1

print(result)