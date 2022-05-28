a = int(input())
ten = a//10
one = a%10
new = 0
count = 0

while 1:
    new = ten + one
    new = one*10 + new%10
    ten = new//10
    one = new%10
    count += 1
    if new == a:
        break

print(count)