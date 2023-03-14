from no1_primeRow import PrimeRow
from no2_primeBox import PrimeBox
from no3_primeBox2 import PrimeBox2
from no4_factorial import FactorialRow
from no5_addition import AddingRow
from no6_tri import TriPattern
from no7_tri2 import TriPattern2
from no8_tri3 import TriPattern3
from no9_tri4 import TriPattern4

sel = -1
sel2 = 0

while sel != 0 and sel < 10:
    if sel == -1:
        print("MENU SELECTION")
        print("======================================")
        print("1. Prime Numbers n times")
        print("2. Prime Numbers in n x n")
        print("3. Prime Numbers in n x n - Continuous")
        print("4. Factorial of n + Formula")
        print("5. Additions to n + Formula")
        print("6. Triangle Pattern from n")
        print("7. Upside Down Triangle Pattern")
        print("8. Diamond Pattern from n")
        print("9. Hourglass Pattern from n")
        print("10. Exit (Alt: 0)")

        sel = int(input("Input: "))

    if sel == 1:
        num = int(input("Input a number to display prime numbers: "))
        prime = PrimeRow(num)
        prime.printRow()
    elif sel == 2:
        num = int(input("Input a number to display prime numbers in n x n: "))
        prime = PrimeBox(num)
        prime.printBox()
    elif sel == 3:
        num = int(input("Input a number to display prime numbers in n x n: "))
        prime = PrimeBox2(num)
        prime.printBox()
    elif sel == 4:
        num = int(input("Input a number to factorialize: "))
        factorial = FactorialRow(num)
        factorial.printRow()
    elif sel == 5:
        num = int(input("Input a number to add from 1 to n: "))
        add = AddingRow(num)
        add.printRow()
    elif sel == 6:
        num = int(input("Input a number to draw a triangle pattern: "))
        tri = TriPattern(num)
        tri.printPattern()
    elif sel == 7:
        num = int(input("Input a number to draw an upside down triangle pattern: "))
        tri = TriPattern2(num)
        tri.printPattern()
    elif sel == 8:
        num = int(input("Input a number to draw a diamond pattern: "))
        diamond = TriPattern3(num)
        diamond.printPattern()
    elif sel == 9:
        num = int(input("Input a number to draw an hourglass pattern: "))
        glass = TriPattern4(num)
        glass.printPattern()
    
    if sel != 0 and sel < 10:
        print("Would you like to return to the menu?")
        print("1. No")
        print("2. Yes")
        sel2 = int(input("Input: "))

        if sel2 % 2 == 0:
            sel = -1
        
        sel2 = 0