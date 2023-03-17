var btnTema = document.querySelector('.btnTema');
var miBody = document.getElementById('miBody');
var btnSubir = document.getElementById('btnSubir');

// Cambia a tema oscuro (JS + CSS)
btnTema.onclick = function() {
    btnTema.classList.toggle('dark');
    miBody.classList.toggle('dark');
}

// Loader (Cuando termine de cargar página)
window.onload = function() {
    $('#loaderBox').fadeOut(); // Desaparece loader con Jquery
    $('body').removeClass('hidden'); // Remover class hidden del body
}

// Script btnSubir
window.onscroll = () => {
    
    // Mostrar o desaparecer dependiendo del Scroll value
    if (document.documentElement.scrollTop > 100) {
        btnSubir.classList.add('mostrar');
    } else {
        btnSubir.classList.remove('mostrar');
    }
    
    // Al hacer click
    btnSubir.addEventListener('click', () => {
        window.scrollTo({top: 0, behavior: 'smooth'})
    })
}