class NumberRow():
    def __init__(self):
        self.getNumber()
        self.printRow()

    def getNumber(self):
        try:
            self.n = int(input("Input a number (divisible by 3, 3-60 range, int): "))
        except ValueError:
            print("Value inserted is not valid. (ERR ID 0)")
            self.getNumber()
        else:
            if self.n > 60 or self.n < 3 or self.n % 3 != 0:
                print("Value inserted doesn't fit the criteria. (ERR ID 1)")
                self.getNumber()

    def printRow(self):
        text = ""
        file = open("homework3/output.txt", "a")
        file.write("== OUTPUT NO. 6 ==\n")

        # 3 + 6 + 9 + 12 + 15 + 18... (multiple of 3)
        result = 0
        for i in range(1, self.n + 1):
            text += f"{3 * i} "
            result += 3 * i

            if i != self.n:
                text += "+ "
            else:
                text += "= "
        text += f"{result}\n"

        # 2 x 3 x 5 x 7 x 11 x 13... (prime)
        result = 1
        done = 0
        m = 1
        primeScore = 0

        while done < self.n:
            for i in range(1, m + 1):
                if m % i == 0:
                    primeScore += 1

                if primeScore > 2:
                    break
            
            if primeScore == 2:
                text += f"{m} "
                result = result * m
                done += 1

                if done != self.n:
                    text += "x "
                else:
                    text += "= "
            
            primeScore = 0
            m += 1
        text += f"{result}\n"

        # 5 + 10 + 30 + 120 + 600 + 3600...
        result = 0
        m = 5

        for i in range(1, self.n + 1):
            m = m * i
            result += m
            text += f"{m} "

            if i != self.n:
                text += "+ "
            else:
                text += "= "
        text += f"{result}"

        print(text)
        file.write(f"{text}\n")
        file.close()