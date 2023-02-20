n = int(input('Masukkan satu bilangan: '))
primeScore = 1 #bilangan prima jika scorenya 2 (dibagi 1 dan n)

for i in range(1, n + 1):
    if n % (i + 1) == 0:
        primeScore += 1

if primeScore == 2:
    print(f'{n} adalah bilangan prima.')
else:
    print(f'{n} bukanlah bilangan prima.')