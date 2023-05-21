class FibonacciRow():
    a = 1
    b = 0
    c = 1

    def __init__(self):
        self.getNumber()
        self.printRow()

    def getNumber(self):
        try:
            self.n = int(input("Input a number (integer): "))
        except ValueError:
            print("Value inserted is not valid.")
            self.getNumber()
    
    def printRow(self):
        text = ""
        file = open("homework3/output.txt", "a")
        file.write("== OUTPUT NO. 1 ==\n")

        for i in range(self.n):
            text += f"{self.a} "
            self.a = self.b + self.c
            self.b = self.c
            self.c = self.a
        
        print(text)
        file.write(f"{text}\n")
        file.close()