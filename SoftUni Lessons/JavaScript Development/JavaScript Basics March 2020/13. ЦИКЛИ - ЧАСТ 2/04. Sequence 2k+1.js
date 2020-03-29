function sequance2kPlus1 (params) {
    let num = Number(params.shift());

    let current = 1;

    while (current <= num) {
        console.log(current);
        current = current * 2 + 1;
    }
}

sequance2kPlus1([3]) // Expected Output:
// 1
// 3

sequance2kPlus1([8]) // Expected Output:
// 1
// 3
// 7 