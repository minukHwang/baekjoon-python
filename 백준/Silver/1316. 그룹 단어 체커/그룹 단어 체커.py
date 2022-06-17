count = 0

def word_repeat(a):
    cnt = 0
    b = []
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            b.append(a[i-1])
        if i == len(a)-1:
            b.append(a[i])
    c = set(b)    
    if len(b) == len(c):
        cnt += 1
    return cnt

n = int(input())

for i in range(n):
    a = list(input())
    count += word_repeat(a)

    
print(count)