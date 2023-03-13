class TriPattern():
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