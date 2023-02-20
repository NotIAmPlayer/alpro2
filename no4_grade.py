nilai = float(input('Masukkan nilai akhir: '))

if nilai > 80:
    grade = "A"
elif nilai > 75:
    grade = "B+"
elif nilai > 70:
    grade = "B"
elif nilai > 65:
    grade = "C+"
elif nilai > 60:
    grade = "C"
elif nilai > 45:
    grade = "D"
else:
    grade = "E"

print(f'Dengan nilai {nilai}, gradenya adalah {grade}.')