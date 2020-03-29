function cake(data) {
    let size = (Number(data.shift())) * (Number(data.shift()));
    let sum = 0;

    while("I say so") {
        let part = data.shift();
        if (part === 'STOP') {break;}
        sum += Number(part);
        if (size < sum) {break;}
    }

    if (size < sum) {
        console.log(`No more cake left! You need ${sum - size} pieces more.`);
    } else {
        console.log(`${size - sum} pieces are left.`);
    }
}


cake([10, 10, 20, 20, 20, 20, 21]);  // Expected Output:
// No more cake left! You need 1 pieces more.

cake([10, 2, 2, 4, 6, 'STOP']);  // Expected Output:
// 8 pieces are left.
