n = int(input())
count = 1
stack = []
push_pop = []
    
for i in range(n):
    data = int(input())
    while count <= data :
        stack.append(count)
        push_pop.append("+")
        count += 1 
    if stack[-1] == data:
        stack.pop()
        push_pop.append("-")
    else:
        print("NO")
        break
        
if len(stack) == 0:
    for item in push_pop:
        print(item)
