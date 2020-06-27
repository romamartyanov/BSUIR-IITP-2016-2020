

// 19. В поликлинике генерируется список талонов к врачу. Каждый пункт
// списка содержит: дату, время, номер очереди, ФИО больного (изначально поле
// пустое), номер кабинета, ФИО врача. Генерация талонов происходит на
// неделю, начиная с введенной даты, в соответствии с графиком работ врачей.
// График работы врача содержит: специализацию врача, ФИО врача, временной
// диапазон работы на каждый день с понедельника по субботу (длительность
// приема врачом больного – 15 минут). Требуется:
// сформировать списки талонов к врачу;
// осуществлять поиск всех записей к врачу на конкретную дату;
// осуществлять поиск записей о больном по ФИО.


Date.prototype.addMinutes = function (min) {
    this.setTime(this.getTime() + (min * 60000));
    return this;
}

Date.prototype.addHours = function (h) {
    this.setTime(this.getTime() + (h * 3600000));
    return this;
}

let randomInt = (min, max) => Math.round(min + Math.random() * (max - min));

const DoctorType = {
    NURSE: "NURSE",
    ALLERGIST: "ALLERGIST",
    PHLEBOLOGIST: "PHLEBOLOGIST",
    RADIOLOGIST: "RADIOLOGIST",
    GYNECOLOGIST: "GYNECOLOGIST",
    OTOLARYNGOLOGIST: "OTOLARYNGOLOGIST",
};

const WeekDay = {
    SUNDAY: 0,
    MONDAY: 1,
    TUESDAY: 2,
    WEDNESDAY: 3,
    THURSDAY: 4,
    FRIDAY: 5,
    SATURDAY: 6
}

class Person {

    constructor(fullName) {
        this.fullName = fullName;
    }
}

class Patien extends Person {

    constructor(fullName) {
        super(fullName);
    }
    toString() {
        return `${this.fullName}`
    }
}

class Doctor extends Person {

    constructor(fullName, doctorType, workInterval, weekends) {
        super(fullName);
        this.doctorType = doctorType;
        this.workInterval = workInterval;
        this.weekends = weekends;
    }

    toString() {
        return `\nВрач: ${this.fullName}, ${this.doctorType}`;
    }

}

class Ticket {

    constructor(date, queueNum, doctor, cabinetNum) {
        this.date = date.toLocaleDateString();
        this.time = date.toLocaleTimeString();
        this.queueNum = queueNum;
        this.doctor = doctor;
        this.cabinetNum = cabinetNum;
        this.patien = null;
    }

    setPatien(patien) {
        this.patien = patien;
    }

    getPatien() {
        return this.patien;
    }

    toString() {
        var patien = this.patien === null ? `Больной: отсутствует` : `Больной: ${this.patien}`;
        return `Талон к врачу: ${this.doctor}\nДата: ${this.date}\n` +
            `Время: ${this.time}\nНомер в очереди: ${this.queueNum}\nНомер кабинета: ${this.cabinetNum}\n` + patien;
    }
}

class Hospital {

    constructor() {
        this.doctors = [];
        this.tickets = [];
    }

    addDoctor(doctor) {
        this.doctors.push(doctor);
    }

    removeDoctor(doctor) {
        var i = this.doctors.indexOf(doctor);
        if (i > -1) {
            this.doctors.splice(i, 1);
        }
    }

    addTicket(ticket) {
        this.tickets.push(ticket);
    }

    generateTicket(doctor, startDate) {
        var i = this.doctors.indexOf(doctor);
        if (i > -1) this.doctors[i];
        else this.addDoctor(doctor);

        for (var i = 0; i < 7; i++) {
            if (!(doctor.weekends.includes(startDate.getDay()))) {
                startDate.setHours(8, 0, 0, 0);
                startDate.addMinutes(-doctor.workInterval);
                var cabinetNum = randomInt(40, 45);
                for (var j = 0; j < 480 / doctor.workInterval; j++) {
                    this.addTicket(new Ticket(startDate.addMinutes(doctor.workInterval), j + 1, doctor, cabinetNum));
                }
                startDate.addMinutes(doctor.workInterval);
            }
            startDate.setDate(startDate.getDate() + 1);
        }
    }

    getTicketsByDate(date, doctorType) {
        var tickets = [];
        for (var t of this.tickets) {
            if (t.date === date.toLocaleDateString()
                && t.doctor.doctorType === doctorType) {
                tickets.push(t);
            }
        }
        return tickets;
    }

    getFirstFreeTicket(date, doctorType) {
        for (var t of this.getTicketsByDate(date, doctorType)) {
            if (t.getPatien() === null) return t;
        }
        return null;
    }

    printTickets(tickets) {
        for (var t of tickets) {
            console.log(t.toString());
        }
    }

    burnPatient(patient, date, doctorType) {
        var ticket = this.getFirstFreeTicket(date, doctorType);
        if (ticket === null) {
            console.log("Нет свободной даты!");
            return;
        }
        ticket.setPatien(patient);
    }

    getPatientTickets(patient) {
        var tickets = []
        for (var t of this.tickets) {
            if (t.patien === patient) tickets.push(t)
        }
        return tickets;
    }

}


var hosp_1 = new Hospital();
var doctor_1 = new Doctor("Петров Алексей Ивановичи", DoctorType.ALLERGIST, 45, [WeekDay.SATURDAY, WeekDay.SUNDAY]);
var patien_1 = new Patien("Васильев Максим Серьгеевич");
console.log(doctor_1);
hosp_1.generateTicket(doctor_1, new Date(2019, 01, 5));
/*
hosp_1.tickets.forEach(t => {
    console.log(t.toString());
});
*/
hosp_1.burnPatient(patien_1, new Date(2019, 01, 6), DoctorType.ALLERGIST);
hosp_1.burnPatient(patien_1, new Date(2019, 01, 8), DoctorType.ALLERGIST);
//hosp_1.printTickets(hosp_1.getTicketsByDate(new Date(2019, 01, 6), DoctorType.ALLERGIST));
hosp_1.printTickets(hosp_1.getPatientTickets(patien_1));