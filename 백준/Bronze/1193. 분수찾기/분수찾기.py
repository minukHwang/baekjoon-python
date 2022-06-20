a = int(input())
n = 0

while a > 0:
    if a <= n*(n+1)/2:
        break
    n += 1

step = a-(n-1)*(n)//2

if n % 2 != 0 :
    son = n - step + 1
    mother = 1 + step - 1
else :
    son = 1 + step - 1
    mother = n - step + 1

print(str(son) + "/" + str(mother))
