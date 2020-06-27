// Многоквартирный дом характеризуется следующими тремя показателями:
// этажность, число подъездов, количество квартир на этаже. Скрипт запрашивает
// эти показатели и номер квартиры. Выводится номер подъезда, в котором
// находится указанная квартира. При вводе некорректных данных предусмотреть
// генерацию исключительных ситуаций.

function getInt(mes, limit) {
    while (true) {
        var val = +prompt("Введите " + mes, '');
        if (!(val % 1 === 0) || val <= 0 || val > limit) alert('Неверный ввод - повторите');
        else return val;
    }
}

var floor = getInt("Количество этажей:", 200);
if (floor > 5) {
  alert(`Варламов triggered !!1!`);
}

var porch = getInt("Количество подъездов:", 200);

var flat_at_floor = getInt("Количество квартир на этаже:", 1000);

var flat_count = floor * porch * flat_at_floor;
var searching_flat = getInt("Номер квартиры (0 - " + flat_count + "):", flat_count);
var flat_in_porch = floor * flat_at_floor;
var search = 0;

for (var i = 0; i < porch; i++) {
    search += flat_in_porch;
    if (search >= searching_flat) {
        alert(`Номер подъезда: ${i + 1}`);
        break;
    }
}
