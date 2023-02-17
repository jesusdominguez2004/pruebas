# Algortimo "Nota estudiante"

# Captura de información
notaEstudiante = eval(input("Ingrese la nota del estudiante: "))

# Iteración 1
if notaEstudiante >= 0 and notaEstudiante < 5.0:
    # Iteración 2
    if notaEstudiante > 2.95:
        print("El estudiante aprobó (Nota: ", round(notaEstudiante,1), ")")
    # Iteración 3
    if notaEstudiante < 2.95:
        print("El estudiante reprobó (Nota: ", round(notaEstudiante, 1),")")
# Iteración 4
if notaEstudiante <= 0 or notaEstudiante > 5.0:
    print("Nota no válida.")