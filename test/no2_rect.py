class Rect():
    p = 0
    l = 0
    area = 0

    def __init__(self):
        self.getBase()
        self.getHeight()
        self.printResults()
    
    def getBase(self):
        try:
            self.p = float(input("Input nilai panjang dari persegi panjang: "))
        except ValueError:
            print("Input tidak valid.")
            self.getBase()
    
    def getHeight(self):
        try:
            self.l = float(input("Input nilai lebar dari persegi panjang: "))
        except ValueError:
            print("Input tidak valid.")
            self.getHeight()
    
    def printResults(self):
        self.area = self.p * self.l

        f = open("output.txt", "a")
        text = ""

        text += "OUTPUT NO. 2\n"
        text += f"Panjang = {self.p}\n"
        text += f"Lebar   = {self.l}\n"
        text += f"Luas    = {self.p} x {self.l} = {self.area}\n"

        print(text)
        f.write(text)
        f.close()