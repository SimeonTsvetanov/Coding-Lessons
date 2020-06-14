function solution() {
    let str = '';
    return {
        append(string) {
            return str += string;
        },
        removeStart(n) {
            return str = str.slice(n);
        },
        removeEnd(n) {
            return str = str.slice(0, str.length -n);
        },
        print() {
            return console.log(str);
        }
    };
}

let firstZeroTest = solution();
firstZeroTest.append('hello');
firstZeroTest.append('again');
firstZeroTest.removeStart(3);
firstZeroTest.removeEnd(4);
firstZeroTest.print();  // loa

let secondZeroTest = solution();
secondZeroTest.append('123');
secondZeroTest.append('45');
secondZeroTest.removeStart(2);
secondZeroTest.removeEnd(1);
secondZeroTest.print();  // 34
