

// На декартовой плоскости прямоугольник задаётся четырьмя точками –
// своими вершинами (у каждой точки две числовые координаты). Вершины
// перечисляются последовательно, в порядке обхода по часовой стрелке,
// начиная с произвольной вершины.

// 1. Написать функцию, проверяющую, образуют ли заданные восемь
// чисел вершины некоего прямоугольника.

// 2. Написать функцию, проверяющую принадлежность указанной точки
// заданному прямоугольнику.


function getInt(mes, limit) {
    while (true) {
        var val = +prompt("Введите " + mes, '');
        if (!(val % 1 === 0) || val > limit) alert('Неверный ввод, повторите!');
        else return val;
    }
}

function lineLen(start, end) {
    let x1 = start[0];
    let y1 = start[1];
    let x2 = end[0];
    let y2 = end[1];
    return (Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
}

function isRect(points) {
    let a1 = lineLen(points[0], points[1]);
    let b1 = lineLen(points[1], points[2]);

    let a2 = lineLen(points[2], points[3]);
    let b2 = lineLen(points[3], points[0]);

    let c = lineLen(points[2], points[0]);

    if (isRightTriangle(a1, b1, c)
        && isRightTriangle(a2, b2, c)) return alert('Фигура - прямоугольник')
    else return alert('Не прямоугольник')
}

function isRightTriangle(a, b, c) {
    return a + b === c;
}


function isInRect(xy, points){

}

let a1 = getInt("точку a1", 100000);
let a2 = getInt("точку a2", 100000);
let b1 = getInt("точку b1", 100000);
let b2 = getInt("точку b2", 100000);
let c1 = getInt("точку c1", 100000);
let c2 = getInt("точку c2", 100000);
let d1 = getInt("точку d1", 100000);
let d2 = getInt("точку d2", 100000);

let point1, point2, point3, point4;
point1 = [a1, a2];
point2 = [b1, b2];
point3 = [c1, c2];
point4 = [d1, d2];
let points = [point1, point2, point3, point4];


isRect(points)

if (getint("2 чтобы перейти ко второму заданию:", 10000) === 2) {
    if (isInRect([getInt("x ", 10000), getInt("y", 10000)], points))
        alert("ваша точка принадлежит прямоугольнику");
    else alert("ваша точка НЕ принадлежит прямоугольнику");
}