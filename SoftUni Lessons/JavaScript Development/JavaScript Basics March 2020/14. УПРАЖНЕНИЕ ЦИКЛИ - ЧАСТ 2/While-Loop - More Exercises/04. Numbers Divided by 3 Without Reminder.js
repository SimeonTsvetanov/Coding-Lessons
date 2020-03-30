function devisionByThree(params) {
    let start = 1;
    let stop = 100;

    while (start <= stop) {
        if (start % 3 == 0) {
            console.log(start);
        }
        start += 1;
    }
}

devisionByThree();
// Expected Output:
// 3
// 6
// 9
// …
// 99
