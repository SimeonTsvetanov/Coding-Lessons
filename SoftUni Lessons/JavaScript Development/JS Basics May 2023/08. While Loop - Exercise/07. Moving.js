function solution(params) {
    // MasK
    let size = Number(params.shift()) * Number(params.shift()) * Number(params.shift());

    while (params.length > 0) {
        boxes = params.shift();
        if (boxes === 'Done') {break;}
        size -= Number(boxes);
        if (size <= 0) {break;}
    }

    let happy = `${size} Cubic meters left.`;
    let sad = `No more free space! You need ${Math.abs(size)} Cubic meters more.`;

    (size < 0) ? console.log(sad) : console.log(happy);
}

solution(["10", 
"10",
"2",
"20",
"20",
"20",
"20",
"122"])

// No more free space! You need 2 Cubic meters more.

console.log('********************************');

solution(["10", 
"1",
"2",
"4", 
"6",
"Done"])

// 10 Cubic meters left.
