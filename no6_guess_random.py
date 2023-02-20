import random
trueNumber = random.randint(1, 99)
chances = 3
correct = False

while (chances > 0) and (not correct):
    guess = int(input('Masukan satu bilangan, dari 1 sampai 99: '))

    if guess == trueNumber:
        print('Anda benar!')
        correct = True
    elif (guess != trueNumber) and (abs(guess - trueNumber) > 20):
        print('Anda salah, tebakan anda terlalu tinggi.')
        chances -= 1
    elif (guess != trueNumber) and (abs(guess - trueNumber) <= 20):
        print('Anda salah, tebakan anda terlalu rendah.')
        chances -= 1

if chances == 0 and (not correct):
    print(f'Jawabannya adalah {trueNumber}.')