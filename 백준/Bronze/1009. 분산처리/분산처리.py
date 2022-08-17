n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    a = a%10
    if a == 0:
        number = 10
    elif a in [1,5,6]:
        number = a
    elif a in [4,9]:
        number = a**2%10 if b%2 == 0 else a%10
    elif a in [2,3,7,8]:
        number = a**(4 if b % 4 == 0 else b % 4)%10
    print(number)