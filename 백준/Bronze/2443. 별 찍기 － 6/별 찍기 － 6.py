n = int(input())
total = 2*n -1

for i in range(n):
    blanks = i
    stars = total - 2*blanks
    print(" "*i + "*" * stars)