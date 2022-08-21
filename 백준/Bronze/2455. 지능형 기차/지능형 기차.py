people = []
total = 0

for i in range(4):
    o, i = map(int,input().split())
    total = total - o + i
    people.append(total)

print(max(people))