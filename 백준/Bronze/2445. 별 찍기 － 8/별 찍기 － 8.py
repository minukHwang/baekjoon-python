n = int(input())

for i in range(1,2*n):
    if i<n:
        print("*"*i+" "*(2*(n-i))+"*"*i)
    elif i == n:
        print("*"*(2*n))
    else:
        print("*"*(2*n-i)+" "*(2*i-2*n)+"*"*(2*n-i))