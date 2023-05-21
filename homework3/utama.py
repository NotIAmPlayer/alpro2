from no1_fibonacci              import FibonacciRow
from no2_starPattern            import StarPattern
from no3_starPattern_reversed   import StarPattern2
from no4_fibonacci_pattern      import FibonacciPattern
from no5_dotted_square          import DottedSquare
from no6_number_rows            import NumberRow

def menu():
    print("SELECTION")
    print("========================")
    print("1. Fibonacci Row")
    print("2. Star Pattern")
    print("3. Reversed Star Pattern")
    print("4. Fibonacci Pattern")
    print("5. Dotted Square Pattern")
    print("6. Number Rows")
    print("0. EXIT")
    print("\nChoose:")
    try:
        n = int(input("> "))
    except ValueError:
        print("Value inserted is not valid. (ERR ID 0)")
        temp = input("Input anything to return... ")
        menu()
    else:
        if n > 6 or n < 0:
            print(f"Option {n} is not available (ERR ID 1)")
            temp = input("Input anything to return... ")
            menu()
        else:
            runProgram(n)

def runProgram(programNum: int) -> None:
    if programNum == 1:
        currentClass = FibonacciRow()
    elif programNum == 2:
        currentClass = StarPattern()
    elif programNum == 3:
        currentClass = StarPattern2()
    elif programNum == 4:
        currentClass = FibonacciPattern()
    elif programNum == 5:
        currentClass = DottedSquare()
    elif programNum == 6:
        currentClass = NumberRow()
    
    if programNum == 0:
        exit()
    else:
        returnToMenuPrompt(programNum)

def returnToMenuPrompt(programNum: int) -> None:
    print("Return to the main menu? (Y/N)")

    try:
        sel = input("> ")
    except (sel != "y" and sel != "Y" and sel != "n" and sel != "N"):
        print("Please enter either Y or N in uppercase or lowercase.")
        temp = input("Input anything to return... ")
        returnToMenuPrompt()
    else:
        if sel == "n" or sel == "N":
            runProgram(programNum)
        else:
            menu()

menu()