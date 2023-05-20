class DottedSquare():
    def __init__(self):
        self.getNumber()
        self.printPattern()

    def getNumber(self):
        try:
            self.n = int(input("Input a number (odd number >= 5): "))
        except ValueError:
            print("Value inserted is not valid. (ERR ID 0)")
            self.getNumber()
        else:
            if ((self.n - 1) % 2 == 1) or self.n < 5:
                print("Value inserted doesn't fit the criteria. (ERR ID 1)")
                self.getNumber()
    
    def printPattern(self):
        text = ""
        file = open("homework3/output.txt", "a")
        file.write("== OUTPUT NO. 5 ==\n")

        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                valid = False
                checkHorizontal = (i == 1) or (i == self.n)
                checkVertical = (j == 1) or (j == self.n)
                checkCenter = ((i == self.n//2 + 1) and (j == self.n//2 + 1))

                if checkHorizontal or checkVertical or checkCenter:
                    valid = True
                
                if valid:
                    text += "* "
                else:
                    text += "  "
            
            if i != self.n:
                text += "\n"
        
        print(text)
        file.write(f"{text}\n")
        file.close()

a = DottedSquare()