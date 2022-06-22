num = int(input())

memory = [0]*1001
memory[1] = 1
memory[2] = 2

for i in range(3,1001):
    memory[i] = memory[i-1] + memory[i-2]

print(memory[num]%10007)