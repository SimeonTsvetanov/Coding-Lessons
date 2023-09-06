function mask (params) {
    // MASK
    let count = params;
    let num = 1;
    let sum = 0;

    while (count > 0) {
        if (num % 2 !== 0) {
            console.log(num);
            sum += num;
            count--;
        }
        num++;
    }

    console.log(`Sum: ${sum}`);
}

mask(5);
//

mask(3);
//
