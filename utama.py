from oop_odd_even import Number

def main():
    menuSelected = -1
    num = 0
    menuOption = ""
    while (menuSelected < 11) and (menuSelected != 0):
        if menuSelected == -1:
            print("MENU\n===========")
            print("1. Bilangan Ganjil/Genap\n2. Luas Segitiga\n3. Luas Lingkaran\n4. Nilai ke Grade")
            print("5. Fibonacci dari n\n6. Tebak Angka\n7. Pola Bintang dari n\n8. Pola bintang dari n - 2")
            print("9. Pola Fibonacci dari n\n10. Bilangan Prima\n11. EXIT")
            menuSelected = int(input("Pilih: "))

            if menuSelected < 0:
                menuSelected = menuSelected * -1

        if menuSelected == 1:
            num = int(input('Masukkan satu bilangan: '))

            numClass = Number(num)
            numClass.oddEven()

            if numClass.even:
                print(f"{num} adalah bilangan genap.")
            else:
                print(f"{num} adalah bilangan ganjil.")
        
        if (menuSelected < 11) and (menuSelected != 0):
            menuOption = input("Kembali ke menu awal? (Y/N) ")
            if menuOption == "Y" or menuOption == "y":
                menuSelected = -1
            else:
                menuSelected = menuSelected
                

if __name__ == "__main__":
    main()