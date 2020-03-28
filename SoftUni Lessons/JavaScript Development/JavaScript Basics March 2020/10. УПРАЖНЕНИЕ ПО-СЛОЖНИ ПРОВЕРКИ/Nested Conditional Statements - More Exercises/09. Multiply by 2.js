function multiplyByTwo(...input) {
    while(true) {
        number = Number(input.shift());
        if (number < 0) {
            console.log('Negative number!')
            break
        } else {
            console.log(`Result: ${(number * 2).toFixed(2)}`)
        }
    }
}

multiplyByTwo([12, 43.2144, 12.3, 543.23, -20]);
multiplyByTwo([23.43, 12.3245, 0, 65.23432, 23, 65, -12]);
multiplyByTwo([-123]);