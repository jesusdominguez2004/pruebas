print('\033[0;91m================================')
print('\033[93m Bienvenido al sistema de rappi')
print('\033[0;91m================================')
print('\033[0;97m   ')
nombre=input('Digite su nombre: ')
clave=int(input('Digite clave del departamento: '))
antiguedad=int(input('Digite años de antiguedad: '))

#departamento de atencion al cliente:
if clave==1 and antiguedad==1:
    print(f'Hola {nombre}, tienes derecho a 6 dias de vacaciones')

elif clave==1 and antiguedad >= 2 and antiguedad <= 6:
    print(f'Hola {nombre}, tienes derecho a 14 dias de vacaciones')

elif clave==1 and antiguedad>=7:
    print(f'Hola {nombre}, tienes derecho a 20 dias de vacaciones')


#departamento de logistica
if clave==2 and antiguedad==1:
    print(f'Hola {nombre}, tienes derecho a 7 dias de vacaciones')

elif clave==2 and antiguedad >= 2 and antiguedad <= 6: 
    print(f'Hola {nombre}, tienes derecho a 15 dias de vacaciones')

elif clave==2 and antiguedad>=7:
    print(f'Hola {nombre}, tienes derecho a 22 dias de vacaciones')

#gerencia
if clave==3 and antiguedad==1:
    print(f'Hola {nombre}, tienes derecho a 10 dias de vacaciones')

elif clave==3 and antiguedad >= 2 and antiguedad <= 6: 
    print(f'Hola {nombre}, tienes derecho a 20 dias de vacaciones')

elif clave==3 and antiguedad>=7:
    print(f'Hola {nombre}, tienes derecho a 30 dias de vacaciones')


