n = int(input())

for i in range(1, 2*n):
    if i <= n:
        blank = n - i
        star = i
    else:
        blank = i - n
        star = 2 * n - i
    
    print(" " * blank + "*" * star)
        