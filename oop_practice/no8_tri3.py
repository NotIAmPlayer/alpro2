class TriPattern3():
    def __init__(self, n: int) -> None:
        self.n = n
    
    def printPattern(self):
        offset = self.n - 1

        for i in range(1, self.n + 1):
            for j in range(1, (self.n * 2 - 1) + 1):
                valid = False
                if i == self.n:
                    valid = True
                if j > offset and j <= (self.n * 2 - 1) - offset:
                    valid = True
                
                if valid:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            
            print("", end = "\n")
            offset -= 1

        offset = 0
        for i in range(self.n + 1, 1, -1):
            for j in range((self.n * 2 - 1), 0, -1):
                valid = False
                if i == self.n + 1:
                    valid = True
                if j > offset and j <= (self.n * 2 - 1) - offset:
                    valid = True
                
                if valid:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            
            print("", end = "\n")
            offset += 1