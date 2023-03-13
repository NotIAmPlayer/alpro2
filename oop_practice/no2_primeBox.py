class PrimeBox():
    def __init__(self, n):
        self.n = n
    
    def printBox(self):
        for z in range(self.n):
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
                    done += 1
                
                primeScore = 0
                m += 1
            print("\n", end="")