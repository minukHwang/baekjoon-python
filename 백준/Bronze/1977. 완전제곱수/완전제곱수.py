import math

m = int(input())
n = int(input())
number = []

int_m = math.ceil(m**(1/2))
int_n = math.floor(n**(1/2))

for i in range(int_m,int_n+1):
    number.append(i**2)

if len(number) == 0:
    print(-1)
else:
    print(sum(number))
    print(min(number))
