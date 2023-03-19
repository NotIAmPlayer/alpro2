from jawabansoalno1 import DottedSquare
from jawabansoalno2 import NumberRows
from jawabansoalno3 import Receipt

sel = -1
sel2 = " "
done = False

while True:
    if sel < 4:
        print("MENU PROGRAM")
        print("1. Pola Bintang Persegi")
        print("2. Pola Deretan Bilangan")
        print("3. Nota Penjualan")

        sel = int(input("Pilih: "))

        if sel < 0:
            sel = sel * -1

    if sel == 1:
        pattern = DottedSquare()
        pattern.inputValue("Masukkan nilai n yang ganjil dan lebih dari 5: ")
        pattern.printPattern()
        done = True
    elif sel == 2:
        numRow = NumberRows()
        numRow.inputValue("Masukkan nilai n antara 3-60 dan berkelipatan 3: ")
        numRow.printRows()
        done = True
    elif sel == 3:
        receipts = []
        total = 0

        while True:
            newReceipt = Receipt()

            noteID = int(input("Masukkan nomor nota penjualan (< 0: Mengakhiri program): "))
            if noteID < 0:
                break
            newReceipt.noteID = noteID

            newReceipt.inputItems()
            newReceipt.countTotal()
            receipts.append(newReceipt)
        done = True

        print(f"\nTOTAL PENJUALAN:")
        print("=============================")
        print("{:<10} {:<20} {:<10} {:<10} {:<10}".format("ID", "Nama", "Harga", "Qty", "Subtotal"))
        for r in receipts:
            for id, name, price, qty in r.items:
                subtotal = price * qty
                total += subtotal
                print(f"{id:<10} {name:<20} {price:<10} {qty:<10} {subtotal:<10}")
        print(f"\nTOTAL: {total}")
    else:
        print(f"Input {sel} tidak ada.")
    
    if done:
        sel2 = input("Lanjutkan berjalannya program? (Y/N): ")

        if sel2.lower() == "n":
            break
        done = False