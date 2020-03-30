function grades(input) {
    // Mask
    let students = Number(input.shift());
    
    let n1 = 0;
    let n2 = 0;
    let n3 = 0;
    let n4 = 0;
    let total = 0;

    for (let student = 1; student <= students; student += 1) {
        score = Number(input.shift());
        total += score

        if (score >= 2 && score <= 2.99) {
            n1 += 1;
        } else if (score >= 3 && score <= 3.99) {
            n2 += 1;
        } else if (score >= 4 && score <= 4.99) {
            n3 += 1;
        } else {
            n4 += 1
        }
    }

    console.log(`Top students: ${(n4 / students * 100).toFixed(2)}%`)
    console.log(`Between 4.00 and 4.99: ${(n3 / students * 100).toFixed(2)}%`)
    console.log(`Between 3.00 and 3.99: ${(n2 / students * 100).toFixed(2)}%`)
    console.log(`Fail: ${(n1 / students * 100).toFixed(2)}%`)
    console.log(`Average: ${(total / students).toFixed(2)}`)
}

grades([10, 3.00, 2.99, 5.68, 3.01, 4, 4, 6.00, 4.50, 2.44, 5]);  // Should return:
// Top students: 30.00%
// Between 4.00 and 4.99: 30.00%
// Between 3.00 and 3.99: 20.00%
// Fail: 20.00%
// Average: 4.06

grades([6, 2, 3, 4, 5, 6, 2.2]);  // Should return:
// Top students: 33.33%
// Between 4.00 and 4.99: 16.67%
// Between 3.00 and 3.99: 16.67%
// Fail: 33.33%
// Average: 3.70
