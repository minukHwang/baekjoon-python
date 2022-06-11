word = input().upper()
letters = set(word)
count = []
max_letter = ""

for letter in letters:
    count.append(word.count(letter))

max_count = max(count)
cnt = 0
    
for letter in letters:
    if word.count(letter) == max_count:
        max_letter = letter
        cnt += 1
    if cnt > 1:
        print("?")
        break

if cnt == 1:
    print(max_letter)