total = 0
min = 100

for i in range(7):
    n = int(input())
    if n % 2 != 0:
        total += n
        if min > n:
            min = n
    
if total == 0:
    print(-1)
else:
    print(total)
    print(min)