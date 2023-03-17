var myText = document.getElementById('myText');
var myLanguage = document.getElementById('myLanguage');

/*document.onclick = function() {
  myText.innerHTML = 'HolaMundo...';
  myText.dataset.text = 'HolaMundo...';
}*/

// Cambiar texto
var numClicks = 0;
document.onclick = function() {
  
  // Variable
  numClicks = numClicks + 1;
  
  // Switch
  switch (numClicks) {
    // Español
    case 1:
      myText.innerHTML = 'HolaMundo...';
      myText.dataset.text = 'HolaMundo...';
      myLanguage.innerHTML = '(Español)';
      break;
    // Portugués
    case 2:
      myText.innerHTML = 'OláMundo...';
      myText.dataset.text = 'OláMundo...';
      myLanguage.innerHTML = '(Portugués)';
    break;
    // Francés
    case 3:
      myText.innerHTML = 'SalutMonde...';
      myText.dataset.text = 'SalutMonde...';
      myLanguage.innerHTML = '(Francés)';
     break;
    // Italiano
    case 4:
      myText.innerHTML = 'CiaoMondo...';
      myText.dataset.text = 'CiaoMondo...';
      myLanguage.innerHTML = '(Italiano)';
    break;
    // Ruso
    case 5:
      myText.innerHTML = 'Приветмир...';
      myText.dataset.text = 'Приветмир....';
      myLanguage.innerHTML = '(Ruso)';
    break;
    // Griego
    case 6:
      myText.innerHTML = 'ΓειάσουΚόσμε...';
      myText.dataset.text = 'ΓειάσουΚόσμε...';
      myLanguage.innerHTML = '(Griego)';
    break;
    // Japonés
    case 7:
      myText.innerHTML = 'こんにちは界...';
      myText.dataset.text = 'こんにちは界...';
      myLanguage.innerHTML = '(Japonés)';
    break;
    // Coreano
    case 8:
      myText.innerHTML = '헬로월드...';
      myText.dataset.text = '헬로월드...';
      myLanguage.innerHTML = '(Coreano)';
    break;
    // Chino tradicional
    case 9:
      myText.innerHTML = '你好世界...';
      myText.dataset.text = '你好世界...';
      myLanguage.innerHTML = '(Chino tradicional)';
    break;
    // Francés
    case 10:
      myText.innerHTML = 'HeiVerden...';
      myText.dataset.text = 'HeiVerden...';
      myLanguage.innerHTML = '(Noruego)';
    break;
    // Volver al principio (Inglés)
    case 11:
      numClicks = 0;
      myText.innerHTML = 'HelloWorld...';
      myText.dataset.text = 'HelloWorld...';
      myLanguage.innerHTML = '(Inglés)';
    break;
  }
}