n = int(input())
num_list = []

for i in range(n):
    num = int(input())
    if num == 0:
        if len(num_list) > 0:
            num_list.pop(-1)
    else:
        num_list.append(num)

print(sum(num_list))