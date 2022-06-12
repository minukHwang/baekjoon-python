a,b = input().split()

def reverse_num(num):
    num = list(num)
    num.reverse()
    num = ''.join(num)
    return int(num)

a = reverse_num(a)
b = reverse_num(b)

if  a>b:
    print(a)
else:
    print(b)