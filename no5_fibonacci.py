n = int(input('Masukkan jumlah bilangan untuk Fibonacci: '))

a = 0
b = 1
c = 0

for i in range(n):
    print(a)
    a = b + c
    b = c
    c = a