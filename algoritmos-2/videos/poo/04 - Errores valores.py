# Errores valores | 04

"""
raise -> lanzar, generar 
assert -> verificar, comprobar
return -> devolver
"""
# Tipo parámetros
def sumar(a: int, b: int) -> int:
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("Ambos argumentos deben ser enteros")
    
    if not isinstance(a, int):
        raise TypeError("a debe ser entero")
    
    if not isinstance(b, int):
        raise TypeError("b debe ser entero")
    
    return a + b

print(sumar(30, 2)) # Normal
# print(sumar(3.14, 10)) # Error parámetro a
# print(sumar(10, 2.17)) # Error parámetro b
# print(sumar(3.14, 2.17)) # Error parámetro a y b

# Tipo valor devuelto
def sumar(a: int, b: int) -> int:
    resultado = a + b
    assert isinstance(resultado, int), "El resultado NO fue entero"
    return resultado

print(sumar(30, 2)) # Normal
# print(sumar("abc", "abc")) # Error resultado str
# print(sumar(10, 2.5)) # Error resultado float
