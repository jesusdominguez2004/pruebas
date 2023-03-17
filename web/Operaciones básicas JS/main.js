var openModal = document.getElementById('openModal');
var closeModal = document.getElementById('closeModal');
var modalBox = document.getElementById('modalBox');

var num1 = document.getElementById('num1');
var num2 = document.getElementById('num2');
var resultado = document.getElementById('resultado');
var operacion = document.getElementById('operacion');
var btnCalcular = document.getElementById('btnCalcular');
var iconOperacion = document.getElementById('iconOperacion');

// Mostrar modal info
openModal.onclick = function() {
    modalBox.classList.add('active');
}
// Ocultar modal info
closeModal.onclick  = function() {
    modalBox.classList.remove('active');
}

// Función procesar operación (Al cambiar select)
operacion.onchange = function procesarOperacion() {
    // parseInt -> convertir una cadena a un entero
    switch (operacion.value) {
        case 'sumar':
            iconOperacion.innerHTML = '+';
            resultado.value = parseInt(num1.value) + parseInt(num2.value);
            break;
        case 'restar':
            iconOperacion.innerHTML = '-';
            resultado.value = parseInt(num1.value) - parseInt(num2.value);
            break;
        case 'multiplicar':
            iconOperacion.innerHTML = 'x';
            resultado.value = parseInt(num1.value) * parseInt(num2.value);
            break;
        case 'dividir':
            iconOperacion.innerHTML = '/';
            resultado.value = parseInt(num1.value) / parseInt(num2.value);
        break;  
    }
}
// Función procesar operación (Al presionar btnCalcular)
btnCalcular.onclick = function procesarOperacion() {
    // parseInt -> convertir una cadena a un entero
    switch (operacion.value) {
        case 'sumar':
            iconOperacion.innerHTML = '+';
            resultado.value = parseInt(num1.value) + parseInt(num2.value);
            break;
        case 'restar':
            iconOperacion.innerHTML = '-';
            resultado.value = parseInt(num1.value) - parseInt(num2.value);
            break;
        case 'multiplicar':
            iconOperacion.innerHTML = 'x';
            resultado.value = parseInt(num1.value) * parseInt(num2.value);
            break;
        case 'dividir':
            iconOperacion.innerHTML = '/';
            resultado.value = parseInt(num1.value) / parseInt(num2.value);
        break;  
    }
}