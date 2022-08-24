n = input()
number = list(input().split())
count = 0

for item in number:
    if item[-1] == n:
        count += 1

print(count)