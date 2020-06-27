// 4. В строке, состоящей из групп нулей и единиц, найти и вывести на
// экран группы с четным количеством символов.

// Из строки, состоящей из букв, цифр, запятых, точек, знаков + и – ,
// выделить подстроку, задающую вещественное число с фиксированной точкой.

function getEvenSymbolsGroup(str) {
  var arr = [];
  var last_c, curr_c;
  var cnt = 0;
  var str_len = str.length
  for (var i = 0; i < str_len; i++) {
    curr_c = str.charAt(i);
    if ("01".indexOf(curr_c) === -1) {
      return -1;
    }
    if (curr_c != last_c) {
      if (cnt != 0 && cnt % 2 === 0) {
        arr.push([i - cnt, i - 1]);
      }
      cnt = 1;
    } else cnt++;

    last_c = curr_c;
  }
  if (cnt % 2 == 0) {
    arr.push([str_len - cnt, str_len - 1]);
  }
  return arr;
}


var ans, str;
while (true) {
  str = prompt("Введите строку, состоящую из нулей и единиц: ", "");
  ans = getEvenSymbolsGroup(str);
  if (ans === -1) alert("Неверный ввод! Повторите: ");
  else break;
}

console.log(str);
console.log(ans);
