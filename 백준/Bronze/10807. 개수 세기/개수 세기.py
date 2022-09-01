n = int(input())
number = list(map(int, input().split()))
v = int(input())
count = 0

for item in number:
    if item == v:
        count += 1
        
print(count)