function devisibleByThree() {
    // Mask
    for (let num = 1; num <= 100; num += 1) {
        if (num % 3 == 0) {
            console.log(num);
        }
    }
}

devisibleByThree();  // Should return:
// 3
// 6
// 9
// ...
// 69
// ...
// 99
