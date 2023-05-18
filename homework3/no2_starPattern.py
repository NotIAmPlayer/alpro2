class StarPattern():
    def __init__(self):
        self.getNumber()
        self.printPattern()

    def getNumber(self):
        try:
            self.n = int(input("Input a number (integer) for the star pattern: "))
        except ValueError:
            print("Value inserted is not valid.")
    
    def printPattern(self):
        text = ""
        file = open("homework3/output.txt", "a")
        file.write("== OUTPUT NO. 2 ==\n")

        for i in range(1, self.n + 1):
            text += "*" * i

            if i != self.n:
                text += "\n"
        
        print(text)
        file.write(f"{text}\n")
        file.close()

a = StarPattern()