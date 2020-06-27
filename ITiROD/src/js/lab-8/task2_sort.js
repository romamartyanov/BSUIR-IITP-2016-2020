

// Создать функцию createMatrix(), принимающую количество строк и
// количество столбцов матрицы и возвращающее матрицу (массив массивов),
// заполненную случайными числами в диапазоне от 0 до 100. Написать функцию,
// выполняющую суммирование двух таких «матриц».

// 4. Дана вещественная матрица размером NxM. Упорядочить ее 
// строки по возрастанию наибольших элементов в строках матрицы.


let randomInt = (min, max) => Math.round(min + Math.random() * (max - min));

function createMatrix(rows, columns) {
    var a = [];
    for (var i = 0; i < rows; i++) {
        var b = [];
        for (var j = 0; j < columns; j++) {
            b.push(randomInt(0, 100));
        }
        a.push(b);
    }
    return a;
}

function sorting(arr, comporator) {
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < arr.length - 1; j++) {
            if (comporator(arr[j], arr[j + 1])) {
                var temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}

function num_compare(left, right) {
    return left > right;
}

function array_compare(left, right) {
    for (var i = 0; i < Math.min(left.length, right.length); i++) {
        if (left[i] === right[i]) continue;
        return left[i] > right[i];
    }
}



function solve(arr) {
    var a = [];
    for (var i = 0; i < arr.length; i++) {
        a.push(sorting(arr[i], num_compare));
    }
    return a;
}

//var a = [34, 203, 3, 746, 200, 984, 198, 764, 9];
//var b = [[34, 21], [3, 1], [203, 4], [3, 0], [746, 14], [200, 201], [984, 84], [198, 12], [764, 417], [9, 0]];
var a = createMatrix(5, 5);
//sorting(b, array_compare);
console.log(solve(a));