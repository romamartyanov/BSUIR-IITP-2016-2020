// Вычисление и вывод i-го числа Фибоначчи, где параметр i вводится пользователем.
// При вводе некорректных данных предусмотреть генерацию исключительной ситуации.


function getInt(mes, limit) {
    while (true) {
        var val = +prompt("Введите " + mes, '');
        if (!(val % 1 === 0) || val <= 0 || val > limit) alert('Неверный ввод - повторите');
        else return val;
    }
}

function fib(n) {
    var a = 1,
        b = 1;
    for (var i = 3; i <= n; i++) {
        var c = a + b;
        a = b;
        b = c;
    }
    return b;
}

alert("Значение i-го числа Фибоначчи: " + fib(getInt('номер i-го числа Фибоначчи:', 1476)));
