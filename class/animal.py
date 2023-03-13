class Animal():
    #constructor
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def move(self) -> None:
        print("Binatang bergerak.")