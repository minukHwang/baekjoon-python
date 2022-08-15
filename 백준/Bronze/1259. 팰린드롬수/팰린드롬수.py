while True:
    n = input()
    if(n == "0"):
        break
    reverse = n[::-1]
    
    if(n == reverse):
        print("yes")
    else:
        print("no")