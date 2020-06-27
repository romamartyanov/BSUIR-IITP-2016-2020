

// Создайте класс Vector для представления вектора в трехмерном
// пространстве (свойства для координат x, y, z). Добавьте в прототип Vector два
// метода plus() и scalar() для вычисления суммы двух векторов и скалярного
// произведения двух векторов. Добавьте в прототип свойство только для чтения
// length, подсчитывающее длину вектора. Переопределите в классе Vector методы
// toString() и valueOf(). Протестируйте созданный класс.


class Vector {

    constructor(x, y, z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    get length() {
        return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2) + Math.pow(this.z, 2));
    }

    set length(value) {
        console.log("This property is read-only");
    }

    plus(vec) {
        this.x += vec.x;
        this.y += vec.y;
        this.z += vec.z;
        return 0;
    }

    scalar(vec) {
        return this.x * vec.x + this.y * vec.y + this.z * vec.z;
    }

    toString() {
        return `Ваш вектор {X: ${this.x}; Y: ${this.y}; Z: ${this.z}}\nДлина = ${this.length}`;
    }

    valueOf() {
        return "[Object Vector]";
    }
}

let a = new Vector(1, 2, 3);
let b = new Vector(4, 5, 6);

a.length = 2019;
console.log(a.length);
console.log(a.toString());
console.log(a.valueOf());
console.log(a.scalar(b));
console.log(a.plus(b));
console.log(a.toString());
