// Diccionario de días de la semana
const days = {
    0: 'Domingo',
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado'
}

// Fecha de nacimiento
let fechaNacimiento = new Date(2004, 04, 07);
// Imprimir resultado
console.log(days[fechaNacimiento.getDay()]);