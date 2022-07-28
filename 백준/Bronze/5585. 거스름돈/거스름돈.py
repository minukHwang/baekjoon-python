n = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
amount = 0;

for item in coin:
    if(n//item > 0):
        amount += n//item
        n -= (n//item) * item
    else:
        continue
    
print(amount)