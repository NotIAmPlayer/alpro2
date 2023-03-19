class Receipt():
    def __init__(self):
        self.noteID = 0
        self.items = []
        self.total = 0
    
    def inputItems(self):
        while True:
            itemID = input("Masukkan kode barang: ")
            itemName = input("Masukkan nama barang: ")
            itemPrice = int(input("Masukkan harga barang: "))
            itemQty = int(input("Masukkan jumlah barang: "))

            self.items.append((itemID, itemName, itemPrice, itemQty))

            redo = input("Lanjutkan mengisikan data barang? (Y/N): ")
            if redo.lower() == "n":
                break
    
    def countTotal(self):
        print(f"\nNOTA PENJUALAN: {self.noteID}")
        print("=============================")
        print("{:<10} {:<20} {:<10} {:<10} {:<10}".format("ID", "Nama", "Harga", "Qty", "Subtotal"))
        for id, name, price, qty in self.items:
            subtotal = price * qty
            self.total += subtotal
            print(f"{id:<10} {name:<20} {price:<10} {qty:<10} {subtotal:<10}")
        print(f"\nTOTAL: {self.total}")