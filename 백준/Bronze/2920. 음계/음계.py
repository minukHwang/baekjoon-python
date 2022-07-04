music = list(map(int, input().split()))
ascending = True
descending = True

for i in range(1, len(music)):
    if music[i-1] < music[i]:
        descending = False
    else:
        ascending = False
        
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")