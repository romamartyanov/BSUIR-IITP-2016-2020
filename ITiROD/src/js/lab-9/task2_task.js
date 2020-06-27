

// Задача имеет название, описание, дату начала и дату окончания. Любая
// задача может иметь набор дочерних подзадач. Создайте класс для
// представления задачи.

// Выполняемая задача – наследник задачи с дополнительным свойствами:
// процент выполнения (число) и флагом задача завершена. Реализуйте данное
// наследование.


class Task {

    constructor(name, description, starDate, endDate) {
        this.name = name;
        this.desc = description;
        this.start = starDate ? starDate.toDateString() : "не задано";
        this.end = endDate ? endDate.toDateString() : "не задано";
        this.subtasks = [];
    }

    add_task(task) {
        this.subtasks.push(task);
    }

    remove_task(task) {
        var i = this.subtasks.indexOf(task);
        if (i > -1) {
            this.subtasks.splice(i, 1);
        }
    }

    taskDesc() {
        return `Ваша задача - ${this.name}\nОписание задачи:\n${this.desc}.\nНачало: ${this.start}, окончание: ${this.end}\n`
    }
}

class ExecutableTask extends Task {

    constructor(name, desc, startDate, endDate, donePercent) {
        super(name, desc, startDate, endDate);
        this.donePercent = donePercent;
        this.isDoneFlag = donePercent === 100;
    }

    taskDesc() {
        const isDone = this.isDoneFlag ? 'Задача завершена' : 'Задача в процессе';
        return super.taskDesc() + `Процент выполнения: ${this.donePercent}%\n${isDone}`;
    }
}

let a = new Task("Бассейн", "Шапочка плавки", null, null);
let b = new ExecutableTask("Хэллоуин пати", "Очень страшная вечеринка", new Date(2019, 9, 31), new Date(2019, 10, 1), 100);

alert(a.taskDesc());
alert(b.taskDesc());
a.add_task(b);
console.log(a);
