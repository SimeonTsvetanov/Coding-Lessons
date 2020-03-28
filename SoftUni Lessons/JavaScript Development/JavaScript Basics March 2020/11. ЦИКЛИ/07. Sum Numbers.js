function sumNumbers(params) {
    let times = Number(params.shift());

    let total = 0;

    for (i = 1; i <= times; i++) {
        total += Number(params.shift());
    }

    console.log(total);
}

sumNumbers([2, 10, 20]);
