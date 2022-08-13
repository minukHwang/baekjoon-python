a,b = input().split()


def maxnmin(num):
    max_num = num
    min_num = num
    
    if num.find("5") != -1:
        max_num = num.replace('5', '6')
                
    if num.find("6") != -1:
        min_num = num.replace('6', '5')
            
    return [int(max_num), int(min_num)]

min_sum = maxnmin(a)[1] + maxnmin(b)[1]
max_sum = maxnmin(a)[0] + maxnmin(b)[0]

print(min_sum, max_sum)