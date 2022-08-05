k = int(input())
length = []
total_width = 0
total_height = 0

for i in range(6):
    a, b = map(int, input().split())
    length.append((a,b))

while True:
    if length[0][0] == length[2][0] and length[1][0] == length[3][0]:
        length = length[0:4]
        break
    else:
        length.append(length.pop(0))
        
for i in range(4):
    if length[i][0] == 1 or length[i][0] == 2:
        total_width += length[i][1]
    elif length[i][0] == 3 or length[i][0] == 4:
        total_height += length[i][1]

area = total_width * total_height - length[1][1] * length[2][1]
total = k * area

print(total)
