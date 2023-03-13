class Number():
    def __init__(self, num: int) -> None:
        self.num = num
    
    def oddEven(self) -> None:
        self.even = False

        if self.num % 2 == 0:
            self.even = True
        
        return self.even