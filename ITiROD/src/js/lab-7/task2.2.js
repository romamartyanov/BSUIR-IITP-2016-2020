

// Декоратор функции получает на вход существующую функцию и
// возвращает новую функцию, изменяющую (дополняющую) поведение
// исходной.
// 2. Создать декоратор для функции с произвольным количеством
// параметров, дополняющий переданную функцию проверкой всех аргумента на
// указанный тип.


function checkType(value, checking_type) {
    return typeof value == checking_type;
}

function typeCheck(f, checks, checking_type) {
    return function () {
        for (var i = 0; i < arguments.length; i++) {
            if (!checks(arguments[i], checking_type)) alert(`Некорректный тип аргумента: ${arguments[i]}`);
        }
        return f.apply(this, arguments);
    }
}

function type() {
    return "Вот это поворот";
}

type = typeCheck(type, checkType, 'number');

alert(type(1));
alert(type(1, 3, 4, "Df"));
alert(type(type()));