import math

class DottedSquare():
    n = 0

    def inputValue(self, prompt: str):
        while not(((self.n - 1) % 2 == 0) and self.n >= 5):
            self.n = int(input(prompt))

            if not(((self.n - 1) % 2 == 0) and self.n >= 5):
                print(f"{self.n} tidak memenuhi ketentuan.")
    
    def printPattern(self):
        for i in range(self.n):
            for j in range(self.n):
                valid = False

                if (i == 0) or (i == self.n - 1):
                    valid = True
                if (j == 0) or (j == self.n - 1):
                    valid = True
                if (i == self.n * 0.5 - 0.5) and (j == self.n * 0.5 - 0.5):
                    valid = True
                
                if valid:
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
            
            print("\n", end = "")