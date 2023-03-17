function clock() {
    var hours = document.getElementById('hours');
    var minutes = document.getElementById('minutes');
    var seconds = document.getElementById('seconds');
    var ampm = document.getElementById('ampm');

    var h = new Date().getHours();
    var m = new Date().getMinutes();
    var s = new Date().getSeconds();

    if(h > 12) {
        h = h - 12;
        var indicator = "PM"; 
    } else {
        var indicator = "AM";
    }

    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;

    hours.innerHTML = h;
    minutes.innerHTML = m;
    seconds.innerHTML = s;
    ampm.innerHTML = indicator;
}

var interval = setInterval(clock, 1000);

// Cada 1s llamar función 'clock'
// The setInterval() method calls a function or evaluates 
// an expression at specified intervals (in milliseconds).
// 1000 ms = 1 second.