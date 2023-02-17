# Ejercicio 3

# Captura de datos:
numeradorFraccion1 = eval(input("Ingrese el numerador de la fracción 1: "))
denominadorFraccion1 = eval(input("Ingrese el denominador de la fracción 1: "))
numeradorFraccion2 = eval(input("Ingrese el numerador de la fracción 2: "))
denominadorFraccion2 = eval(input("Ingrese el denominador de la fracción 2: "))

# Condiciones:
print("- - Resultados - -")
if denominadorFraccion1 != denominadorFraccion2: # fracción heterogenea
    resultadoNumerador = (numeradorFraccion1 * denominadorFraccion2) + (denominadorFraccion1 * numeradorFraccion2)
    resultadoDenominador = denominadorFraccion1 * denominadorFraccion2
    print("Resultado: ", resultadoNumerador, " / ", resultadoDenominador, " = ", round(resultadoNumerador / resultadoDenominador, 4))
    print("Esta es una fracción heterogenea...")
else: # fracción homogenea
    resultadoNumerador = numeradorFraccion1 + numeradorFraccion2
    resultadoDenominador = denominadorFraccion1
    print("Resultado: ", resultadoNumerador, " / ", resultadoDenominador, " = ", round(resultadoNumerador / resultadoDenominador, 4))
    print("Esta es una fracción homogenea...")