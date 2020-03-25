function savings(params) {
    let income = Number(params.shift());
    let months = Number(params.shift()); 
    let needed = Number(params.shift()); 

    let savings = (income - (needed + (income * 0.3)))
    let percentage = (savings / income) * 100;
    let total = months * savings;

    console.log(`She can save ${percentage.toFixed(2)}%`);
    console.log(total.toFixed(2));
}


savings([1500, 3, 800]);  // Expected output:
// She can save 16.67%
// 750.00

savings([2050, 5, 900]);  // Expected Output:
// She can save 26.10%
// 2675.00

savings([3500, 3, 997]);  // Expected Output:
// She can save 41.51%
// 4359.00
