phone = [["A","B","C"], ["D","E","F"], ["G","H","I"], ["J","K","L"], ["M","N","O"], ["P","Q","R","S"], ["T","U","V"], ["W","X","Y","Z"]]
word = input()
total = 0

for item in word:
    for i in range(len(phone)):
        if item in phone[i]:
            total += i+3

print(total)