

// 4. В тексте после указанного символа вставить подстроку.

String.prototype.pasteAfter=function(index, substr) {
    return this.substr(0, index) + substr + this.substr(index);
}


var text = prompt("Введите текст: ", "");
while (true){
   var symbol = prompt("Введите символ: ", "");
   if (symbol.length != 1) alert('Неверный ввод, повторите!');
   else break; 
}
var substr = prompt("Введите подстроку: ", "");

alert(text.pasteAfter(text.indexOf(symbol) + 1, substr))




