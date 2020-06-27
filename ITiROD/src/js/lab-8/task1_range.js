

// Напишите функцию range(), принимающую два аргумента, начало и конец
// диапазона, и возвращающую массив, который содержит все числа из диапазона,
// включая начальное и конечное. Третий необязательный аргумент функции
// range() – шаг для построения массива. Убедитесь, что функция range() работает
// с отрицательным шагом: например, вызов range(5, 2, -1) возвращает [5, 4, 3, 2].


function range(start, end, step) {
    if (typeof step !== 'number') step = 1;
    if ((start > end && step > 0) || (start < end && step < 0) || step === 0) return;
    var arr = [];
    if (step > 0) for (var i = start; i < end; i+=step) arr.push(i);
    else for (var i = start; i > end; i+=step) arr.push(i);
    return arr;
}

alert(range(5, 2, 1))
alert(range(5, 2, -1))
alert(range(1, 5, 2))