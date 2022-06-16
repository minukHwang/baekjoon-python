croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
cnt = 0

for item in croatia:
    cnt += word.count(item)
    word = word.replace(item, '_')

word = word.replace('_','')
cnt += len(word) 
print(cnt)