// 'use strict';

let person = {
    firstName: 'Simeon',
    lastName: 'Tsvetanov',
    fullName: function () { return this.firstName + ' ' + this.lastName; },
    whatIsThis: function () { return this }
}
// console.log(person.fullName());
// console.log(person.whatIsThis());

const moni = {
    age: 30,
    fullName,
    height: 167,
};

const fn = () => {
    console.log(this) // window
}

// console.log(moni.fullName());


function fullName() {
    return this.firstName + ' ' + this.lastName;
}

const simeon = {
    firstName: 'Simeon',
    lastName: 'Tsvetanov',
    fullName() {
        return this.firstName + ' ' + this.lastName;
    },
    getName: () => {
        return this.firstName;
    },
};

// console.log(simeon.fullName());

const test = {
    firstName: 'test1',
    lastName: 'test2',
    fullName: simeon.fullName,
}

// console.log(simeon.getName())

function greet(number) {
    console.log(`${this.name} is number ${number}`);
}

const simeon2 = {name: 'Simeon'};
const iliyana2 = {name: 'Iliyana'};
const moni2 = {name: 'Moni'};

// greet.call(iliyana2, 1); // Argument are given just separated with comma!!!
// greet.call(simeon2, 2);  

// greet.apply(simeon2, [1]); // The arguments age given in Array!!!


const queue = {
    work: [],

    add(fn, priority) {
        this.work.push(fn);
    },

    process() {
        this.work.forEach(fn => fn());
    },
}


const user1 = {
    name: 'user1',
    logName() { console.log(this.name); }
}

const user2 = {
    name: 'user2',
    logName() { console.log(this.name); }
}

const user3 = {
    name: 'user3',
    logName() { console.log(this.name); }
}


queue.add(user1.logName.bind(user1));
queue.add(user2.logName.bind(user2));
queue.add(user3.logName.bind(user3));

// queue.process();

const lib = {
    logFullName() {
        console.log(`${this.firstName} ${this.lastName}`);
    }
}

// ---------------------------------------------
const obj1 = {
    firstName: 'Simeon',
    lastName: 'Tsvetanov',
};

lib.logFullName.call(obj1);
// ----------------------------------------------



