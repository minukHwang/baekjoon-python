n = int(input())
bongji = list()
five = n // 5

for i in range(five+1):
    kg = n - 5 * i
    if kg % 3 == 0:
        bongji.append(kg // 3 + i)

if len(bongji) != 0:
    print(min(bongji))
else:
    print(-1)