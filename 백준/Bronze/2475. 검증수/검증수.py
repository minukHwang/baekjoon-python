a = list(map(int, input().split()))
sum = 0

for item in a:
    sum += item**2

print(sum%10)