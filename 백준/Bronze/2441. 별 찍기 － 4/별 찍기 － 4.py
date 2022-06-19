n = int(input())
star = n
cnt = 0

for i in range(n):
    print(" " * cnt + "*" * star)
    cnt += 1
    star -= 1