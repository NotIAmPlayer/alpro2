class Triangle():
    a = 0
    t = 0
    area = 0

    def __init__(self):
        self.getBase()
        self.getHeight()
        self.printResults()
    
    def getBase(self):
        try:
            self.a = float(input("Input nilai panjang dari persegi panjang: "))
        except ValueError:
            print("Input tidak valid.")
            self.getBase()
    
    def getHeight(self):
        try:
            self.t = float(input("Input nilai lebar dari persegi panjang: "))
        except ValueError:
            print("Input tidak valid.")
            self.getHeight()
    
    def printResults(self):
        self.area = self.a * self.t / 2

        f = open("output.txt", "a")
        text = ""

        text += "OUTPUT NO. 3\n"
        text += f"Alas    = {self.a}\n"
        text += f"Tinggi  = {self.t}\n"
        text += f"Luas    = 0.5 x {self.a} x {self.t} = {self.area}\n"

        print(text)
        f.write(text)
        f.close()