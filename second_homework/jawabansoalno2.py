class NumberRows():
    n = 0

    def inputValue(self, prompt: str):
        while not((self.n >= 3 and self.n <= 60) and (self.n % 3 == 0)):
            self.n = int(input(prompt))

            if not((self.n >= 3 and self.n <= 60) and (self.n % 3 == 0)):
                print(f"{self.n} tidak memenuhi ketentuan.")
    
    def printRows(self):
        for i in range(int(self.n/3)):
            # 3 + 6 + 9 + 12 + 15 + 18... (multiple of 3)
            result = 0
            for j in range(self.n):
                result = result + 3 * (j + 1)
                print(result, end = " ")

                if j != self.n - 1:
                    print("+ ", end = "")
                else:
                    print("= ", end = "")
            print(result)

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
                    print(m, end = " ")
                    result = result * m
                    done += 1

                    if done != self.n:
                        print("x ", end = "")
                    else:
                        print("= ", end = "")
                
                primeScore = 0
                m += 1
            print(result)

            # 5 + 10 + 30 + 120 + 600 + 3600...
            result = 0
            m = 5

            for j in range(self.n):
                m = m * (j + 1)
                result = result + m
                print(m, end = " ")

                if j != self.n - 1:
                    print("+ ", end = "")
                else:
                    print("= ", end = "")
            print(result)