# Ejercicio 1

# Captura de datos:
corte1 = eval(input("Ingrese la nota del corte 1 (0 - 5): "))
corte2 = eval(input("Ingrese la nota del corte 2 (0 - 5): "))
corte3 = eval(input("Ingrese la nota del corte 3 (0 - 5): "))

# Condiciones:
if corte1 < 0 or corte2 < 0 or corte3 < 0 or corte1 > 5 or corte2 > 5 or corte3 > 5:
    print("Datos ingresados no válidos...")
    print("Las notas deben ser números entre 0 y 5...")
else:
    porcentajeCorte1 = corte1 * 0.3 # 30%
    porcentajeCorte2 = corte2 * 0.3 # 30%
    porcentajeCorte3 = corte3 * 0.4 # 40%
    notaFinal = porcentajeCorte1 + porcentajeCorte2 + porcentajeCorte3
    print("- - Resultados - -")
    print("Nota final del estudiante: ", round(notaFinal, 2))
    if notaFinal > 3:
        print("El estudiante aprobó...")
    else:
        print("El estudiante reprobó...")