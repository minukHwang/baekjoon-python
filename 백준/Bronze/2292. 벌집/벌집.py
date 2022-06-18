number = int(input())
i = 0

while i >= 0:
    endpoint = 3*i*(i+1) +1
    if number <= endpoint:
        print(i+1)
        break
    i += 1