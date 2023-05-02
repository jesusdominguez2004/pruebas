let input = document.getElementById("i1");
let p1 = document.getElementById("p1");

function saludar() {
    let nombre = input.innerHTML;
    p1.style.visibility = "visible";
    p1.innerHTML = nombre;
}