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

offset = 0

for i in range(n + 1, 1, -1):
    for j in range((n * 2 - 1), 0, -1):
        valid = False
        if i == n + 1:
            valid = True
        if j > offset and j <= (n * 2 - 1) - offset:
            valid = True
        
        if valid:
            print("*", end = "")
        else:
            print(" ", end = "")
    
    print("", end = "\n")
    offset += 1