n = input()
num_list = list('0123456789ABCDEF')
result = 0

for i in range(len(n)):
    num_index = num_list.index(n[i])
    result += int(num_index * (16 ** (len(n) - i - 1)))

print(result)