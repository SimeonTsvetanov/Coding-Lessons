function sumOfOddNumbers(count) {
    // Mask
    let sum = 0;
    
    let num = 1;
    
    while (count >= 1) {
        if (num % 2 != 0) {
            console.log(num);
            sum += num;
            count--;
        }
        num += 1;
    }
    console.log(`Sum: ${sum}`);
}

sumOfOddNumbers(5);  // Should return:
// 1
// 3
// 5
// 7
// 9
// Sum: 25

sumOfOddNumbers(3);  // Should return:
// 1
// 3
// 5
// Sum: 9
