prime = [True]*1001

m = int(1000**0.5)

for i in range(2,m+1):
    if prime[i] == True:
        for j in range(i+i, 1001, i):
            prime[j] = False
            
prime_num = [i for i in range(2,1001) if prime[i] == True]

n = int(input())
count = 0

numbers = list(map(int, input().split()))

for i in range(n):
    if numbers[i] in prime_num:
        count += 1

print(count)
