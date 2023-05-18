class Rows():
    n = 0

    def __init__(self):
        self.getInput()
        self.printRows()
    
    def getInput(self):
        try:
            self.n = int(input("Input nilai n: "))
        except ValueError:
            print("Input tidak valid.")
            self.getInput()
    
    def printRows(self):
        f = open("output.txt", "a")
        text = ""

        text += "OUTPUT NO. 1\n"
        for i in range(1, self.n + 1):
            text += f"{i} "
        
        print(text)
        f.write(f"{text}\n")
        f.close()