function solution(data) {
    let size = (Number(data.shift())) * (Number(data.shift()));
    let sum = 0;

    while("I say so") {
        let part = data.shift();
        if (part === 'STOP') { break; }
        sum += Number(part);
        if (size < sum) { break; }
    }

    let happy = `No more cake left! You need ${sum - size} pieces more.`;
    let sad = `${size - sum} pieces are left.`;
    (size < sum) ? console.log(happy) : console.log(sad);
}

solution(["10",
"10",
"20",
"20",
"20",
"20",
"21"])

// No more cake left! You need 1 pieces more.

console.log('********************************');

solution(["10",
"2",
"2",
"4",
"6",
"STOP"])

// 8 pieces are left.