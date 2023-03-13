n = 4
offset = n - 1

for i in range(1, n + 1):
    for j in range(1, (n * 2 - 1) + 1):
        valid = False
        if i == n:
            valid = True
        if j > offset and j <= (n * 2 - 1) - offset:
            valid = True
        
        if valid:
            print("*", end = "")
        else:
            print(" ", end = "")
    
    print("", end = "\n")
    offset -= 1