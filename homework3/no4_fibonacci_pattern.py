class FibonacciPattern():
    a = 1
    b = 0
    c = 1

    def __init__(self):
        self.getNumber()
        self.printPattern()

    def getNumber(self):
        try:
            self.n = int(input("Input a number (integer): "))
        except ValueError:
            print("Value inserted is not valid.")
            self.getNumber()
    
    def printPattern(self):
        text = ""
        file = open("homework3/output.txt", "a")
        file.write("== OUTPUT NO. 4 ==\n")

        for i in range(1, self.n + 1):
            for j in range(i):
                text += f"{self.a} "
                self.a = self.b + self.c
                self.b = self.c
                self.c = self.a
            
            if i != self.n:
                text += "\n"
            self.a = 1
            self.b = 0
            self.c = 1
        print(text)
        file.write(f"{text}\n")
        file.close()

a = FibonacciPattern()