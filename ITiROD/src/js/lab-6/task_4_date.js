// 1 января 2015 года – это был четверг. Скрипт запрашивает номер месяца
// (1..12) и число в этом месяце (1..31). Выведите имя дня недели

function getInt(mes, limit) {
    while (true) {
        var val = +prompt("Введите " + mes, '');
        if (!(val % 1 === 0) || val <= 0 || val > limit) alert('Неверный ввод - повторите');
        else return val;
    }
}

var year = getInt("год:");
var month = getInt("номер месяца:", 12);
var day = getInt("день месяца:", 31);
var date = new Date(year, month - 1, day);

var weekday = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
alert(day + "-" + month + "-" + year + " года – это " + weekday[date.getDay()]);