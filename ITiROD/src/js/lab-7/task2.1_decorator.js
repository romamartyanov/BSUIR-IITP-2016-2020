

// Декоратор функции получает на вход существующую функцию и
// возвращает новую функцию, изменяющую (дополняющую) поведение
// исходной.
// 1. Создать декоратор для функции с одним параметром, дополняющий
// переданную функцию проверкой аргумента на тип number.


function checkNumber(value) {
    return typeof value === 'number';
}

function typeCheck(f, checks) {
    return function () {
        if (!checks(arguments[0])) alert("Некорректный тип");
        else return f.apply(this, arguments);
    }
}

function num(a) {
    return a + 1;
}

num = typeCheck(num, checkNumber);

/*alert(num(1));
alert(num("number"));
alert(num(null));*/
alert(num("123"));