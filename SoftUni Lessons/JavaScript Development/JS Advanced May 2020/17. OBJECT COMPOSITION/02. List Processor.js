function listProcessor(commands) {
    // One way of solving:
    /*
    let innerCollection = [];

    commands.map(command => {
        command = command.split(' ');
        command[0] === 'add' ? innerCollection.push(command[1]) : 'ass';
        command[0] === 'remove' ? innerCollection = innerCollection.filter(element => element !== command[1]) : 'pass';
        command[0] === 'print' ? console.log(innerCollection.join(',')) : 'or gas';
    });
     */

    // Second way, using an Object:
        let processor = {
        data: [],
        add: function (str) { return this.data.push(str); },
        remove: function (str) { return this.data = this.data.filter(e => e !== str); },
        print: function () { console.log(this.data.join(',')) },
    };

    commands.map(c => {
        c = c.split(' ');
        c[0] === 'add' ? processor.add(c[1]) : 'ass';
        c[0] === 'remove' ? processor.remove(c[1]) : 'pass';
        c[0] === 'print' ? processor.print() : 'or gas';
    });

}

console.log(listProcessor(['add hello', 'add again', 'remove hello', 'add again', 'print']));  // again,again
console.log(listProcessor(['add pesho', 'add george', 'add peter', 'remove peter','print']));  // pesho,george
