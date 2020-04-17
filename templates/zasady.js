function sprawdzWiek() {
  var x = document.getElementById('wiek');
  try {
    var a = parseInt(x.value);
    if (a < 0 && a > 100) {
      alert("Podaj poprawny wiek");
      x.value = ("Podaj poprawny wiek");
    }
  }
    catch(error){
        x.value = ("Podaj poprawny wiek");
  }
}