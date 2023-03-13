class Mobil():
    # constructor
    def __init__(self, nama: str, cc: int, warna: str) -> None:
        """fungsi memberikan nilai awal kepada mobil"""
        self.nama = nama
        self.cc = cc
        self.warna = warna
    
    jumMobil = 0

    def printSpecs(self) -> None:
        print(f"Nama mobil: {self.nama}")
        print(f"CC mobil: {self.cc}")
        print(f"Warna mobil: {self.warna}")
    
    def addJumMobil(self) -> int:
        Mobil.jumMobil = Mobil.jumMobil + 1
        return Mobil.jumMobil