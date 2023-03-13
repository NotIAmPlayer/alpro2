from mobil import Mobil

def main():
    suzuki = Mobil("Suzuki Ertiga", 1500, "Hitam")
    honda = Mobil("Honda Brio", 1400, "Biru")

    jumMobil = suzuki.addJumMobil()
    jumMobil = honda.addJumMobil()

    suzuki.printSpecs()
    honda.printSpecs()
    print(jumMobil)

if __name__ == "__main__":
    main()