from no1_rows import Rows
from no2_rect import Rect
from no3_tri import Triangle

def runPrograms(n):
    if n == 1:
        varClass = Rows()
    elif n == 2:
        varClass = Rect()
    elif n == 3:
        varClass = Triangle()
    elif n == 0:
        exit()
    
    print("Return to menu? (Y/N)")
    while True:
        try:
            sel2 = input("> ")
        except (sel2 != "Y" and sel2 != "N" and sel2 != "y" and sel2 != "n"):
            print("Selection isn't valid.")
        else:
            print()
            break
    if sel2 == "Y" or sel2 == "y":
        main()
    else:
        runPrograms(n)

def main():
    print("1. Number Rows")
    print("2. Area of Rectangle")
    print("3. Area of Triangle")
    print("0. EXIT")
    print("==== Choose one ====")
    try:
        sel = int(input("> "))
    except ValueError:
        print("Selection isn't valid.")
        a = input("Input anything to return to menu screen.")
        main()
    else:
        if sel > 3 or sel < 0:
            print(f"Selection {sel} isn't available.")
            a = input("Input anything to return to menu screen.")
            main()
        else:
            print()
            runPrograms(sel)

if __name__ == "__main__":
    main()