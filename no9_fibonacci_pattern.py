n = int(input('Masukkan bilangan untuk membuat pola Fibonacci: '))

a = 0
b = 1
c = 0


for i in range(n + 1):
    for j in range(i):
        a = b + c
        b = c
        c = a
        print(a, end = " ")
    print("", end = "\n")
    a = 0
    b = 1
    c = 0