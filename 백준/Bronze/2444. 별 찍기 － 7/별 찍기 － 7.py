n = int(input())
total = 2*n-1

for i in range(1,n):
    stars = 2*i-1
    blanks = int((total - stars) / 2)
    print(" " * blanks + "*" * stars)

for i in range(n):
    blanks = i
    stars = total - 2*blanks
    print(" "*i + "*" * stars)