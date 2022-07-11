word = input()
n = len(word)
a = n // 10

for i in range(a):
    print(word[10*i:10*(i+1)])

print(word[10*a:n])