n, k = map(int, input().split())

def factorial(a):
    a_factorial = 1
    for i in range(1,a+1):
        a_factorial *= i
    return a_factorial
    
c = int(factorial(n)/(factorial(k)*factorial(n-k)))
print(c)