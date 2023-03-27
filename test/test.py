sel = -1
sel2 = 0
sel3 = 0
lang = 0

langTable = [
    ["     SELECTION", "[1] Triangle", "[2] Rectangle", "[3] Square", "[4] Parallelogram", "[1] Area",
     "[2] Perimeter", "Input the base of the triangle: ", "Input the height of the triangle: ",
     "Input the first side of the triangle: ", "Input the second side of the triangle: ",
     "Input the third side of the triangle: ", "Input the length of the rectangle: ",
     "Input the width of the rectangle: ", "Input the length of the square: ",
     "Input the base of the parallelogram: ", "Input the height of the parallelogram: ",
     "Input the first side of the parallelogram: ", "Input the second side of the parallelogram: ",
     "The area of the triangle is ", "The perimeter of the triangle is ", "The area of the rectangle is ",
     "The perimeter of the rectangle is ", "The area of the square is ", "The perimeter of the square is ",
     "The area of the parallelogram is ", "The perimeter of the parallelogram is ", " units."
     ], #English
    ["      Auswahl", "[1] Dreieck", "[2] Rechteck", "[3] Quadrat", "[4] Parallelogramm", 
     "[1] Flächeninhalt", "[2] Umfang", "Geben Sie die Basis des Dreiecks ein: ",
     "Geben Sie die Höhe des Dreiecks ein: ", "Geben Sie die erste Seite des Dreiecks ein: ",
     "Geben Sie die zweite Seite des Dreiecks ein: ", "Geben Sie die dritte Seite des Dreiecks ein: ",
     "Geben Sie die Länge des Rechtecks ein: ", "Geben Sie die Breite des Rechtecks ein: ",
     "Geben Sie die Seitenlänge des Quadrats ein: ", "Geben Sie die Basis de Parallelogramms ein: ",
     "Geben Sie die Höhe de Parallelogramms ein: ", "Geben Sie die erste Siete des Parallelogramms ein: ",
     "Geben Sie die zweite Siete des Parallelogramms ein: ", "Die Flächeninhalt des Dreiecks beträgt ",
     "Der Umfang des Dreiecks beträgt ", "Die Flächeninhalt des Rechtecks beträgt ",
     "Der Umfang des Rechtecks beträgt ", "Die Flächeninhalt des Quadrats beträgt ",
     "Der Umfang des Quadrats beträgt ", "Die Flächeninhalt des Parallelogramms beträgt ",
     "Der Umfang des Parallelogramms beträgt ", " Einheiten."
     ], #Deutsch
    ["     SÉLECTION", "[1] Triangle", "[2] Rectangle", "[3] Carré", "[4] Parallélogramme", "[1] Aire",
     "[2] Périmètre", "Saisissez la base du triangle : ", "Saisissez la hauteur du triangle : ",
     "Saisissez le premier côté du triangle : ", "Saisissez le deuxième côté du triangle : ",
     "Saisissez le troisième côté du triangle : ", "Saisissez la longueur du rectangle : ",
     "Saisissez la largeur du rectangle : ", "Saisissez le côté du carré : ",
     "Saisissez la base du parallélogramme : ", "Saisissez la hauteur du parallélogramme : ",
     "Saisissez le premier côté du parallélogramme : ", "Saisissez le deuxième côté du parallélogramme : ",
     "L'aire du triangle est de ", "Le périmètre du triangle est de ", "L'aire du rectangle est de ",
     "Le périmètre du rectangle est de ", "L'aire du carré est de ", "Le périmètre du carré est de ",
     "L'aire du parallélogramme est de ", "Le périmètre du parallélogramme est de ", " unités."
    ], # Français
    ["     SELECCIÓN", "[1] Triángulo", "[2] Rectángulo", "[3] Cuadrado", "[4] Paralelogramo", "[1] Área",
     "[2] Perímetro", "Ingrese la base del triángulo: ", "Ingrese la altura del triángulo: ",
     "Ingrese el primer lado del triángulo: ", "Ingrese el segundo lado del triángulo: ",
     "Ingrese el tercer lado del triángulo: ", "Ingrese la longitud del rectángulo: ",
     "Ingrese el ancho del rectángulo: ", "Ingrese el lado del cuadrado: ",
     "Ingrese la base del paralelogramo: ", "Ingrese la altura del paralelogramo: ",
     "Ingrese el primer lado del paralelogramo: ", "Ingrese el segundo lado del paralelogramo: ",
     "El área del triángulo es ", "El perímetro del triángulo es ", "El área del rectángulo es ",
     "El perímetro del rectángulo es ", "El área del paralelogramo es ", "El perímetro del paralelogramo es ",
     " unidades."
    ], # Español
    ["     SELEZIONE", "[1] Triangolo", "[2] Rettangolo", "[3] Quadrato", "[4] Parallelogramma", "[1] Area",
     "[2] Perimetro", "Inserisci la base del triangolo: ", "Inserisci l'altezza del triangolo: ",
     "Inserisci il primo lato del triangolo: ", "Inserisci il secondo lato del triangolo: ",
     "Inserisci il terzo lato del triangolo: ", "Inserisci la lunghezza del rettangolo: ",
     "Inserisci la larghezza del rettangolo: ", "Inserisci la lato del quadrato: ",
     "Inserisci la base del parallelogramma: ", "Inserisci l'altezza del parallelogramma: ",
     "Inserisci il primo lato del parallelogramma: ", "Inserisci il secondo lato del parallelogramma: ",
     "L'area del triangolo è ", "Il perimetro del triangolo è ", "L'area del rettangolo è ",
     "Il perimetro del rettangolo è ", "L'area del quadrato è ", "Il perimetro del quadrato è ",
     "L'area del parallelogramma è ", "Il perimetro del parallelogramma è ", " unità."
    ], # Italiano
]

print("LANGUAGE SELECT")
print("====================")
print("[1] English")
print("[2] Deutsch")
print("[3] Français")
print("[4] Español")
print("[5] Italiano")
print("[6] 日本語")
print("[7] Bahasa Indonesia")
lang = int(input())

while True:
    print(langTable[lang - 1][0])
    print("===================")
    print(langTable[lang - 1][1])
    print(langTable[lang - 1][2])
    print(langTable[lang - 1][3])
    print(langTable[lang - 1][4])
    sel = int(input())
    
    if sel != 0:
        print("===================")
        print(langTable[lang - 1][5])
        print(langTable[lang - 1][6])
        sel2 = int(input())
    else:
        break

    if sel == 1:
        if sel2 == 1:
            a = int(input(langTable[lang - 1][7]))
            t = int(input(langTable[lang - 1][8]))

            area = 0.5 * a * t
            print(f"{langTable[lang - 1][19]}{area}{langTable[lang - 1][27]}")
        else:
            a = int(input(langTable[lang - 1][9]))
            b = int(input(langTable[lang - 1][10]))
            c = int(input(langTable[lang - 1][11]))

            perimeter = a + b + c
            print(f"{langTable[lang - 1][20]}{perimeter}{langTable[lang - 1][27]}")