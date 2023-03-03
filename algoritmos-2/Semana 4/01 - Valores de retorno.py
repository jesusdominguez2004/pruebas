# -> es para especificar valor de retorno de la función
from typing import Union, Tuple

# 1. Retorna un solo tipo (int)
def suma(a: int, b: int) -> int:
    return a + b

# 2. Retorna varios tipos con Union[int, None, ...]
def division1(a: int, b: int) -> Union[int, None]:
    if b == 0:
        return None
    else:
        return a // b

# 3. Retorna varios tipos con Tupla (int, float, None, ...)
def division2(a: int, b: int) -> Tuple[int, None]:
    if b == 0:
        return None
    else:
        return a // b
