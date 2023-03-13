class FactorialRow():
    def __init__(self, n: int) -> None:
        self.n = n

    def printRow(self):
        result = 1
        if self.n != 0:
            for i in range(1, self.n + 1):
                result = result * i

                print(i, end = " ")

                if i != self.n:
                    print("x", end = " ")
        else:
            print(1, end = " ")
        
        print(f"= {result}")