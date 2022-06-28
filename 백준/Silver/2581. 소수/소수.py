m = int(input())
n = int(input())
prime = [False]*2+[True]*(n-1)

for i in range(2,int(n**0.5)+1):
    if prime[i] == True:
        for j in range(i+i, n+1, i):
            prime[j] = False
            
prime_num = [i for i in range(m,n+1) if prime[i] == True]

if len(prime_num) == 0:
    print(-1)
else:
    print(sum(prime_num))
    print(prime_num[0])

