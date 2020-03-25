function luggageTax(params) {
    let size = Number(params.shift()) * Number(params.shift()) * Number(params.shift());
    let priority = params.shift();

    let tax = 0

    if (size > 50 && size <= 100) {
        if (priority == 'false') {
            tax = 25;
        }
    } else if (size > 100 && size <= 200) {
        if (priority == 'true') {
            tax = 10;
        } else {
            tax = 50;
        }
    } else if (size > 200 && size <= 300) {
        if (priority == 'true') {
            tax = 20;
        } else {
            tax = 100;
        }
    }

    console.log(`Luggage tax: ${tax.toFixed(2)}`);
}


luggageTax([2, 5, 3, 'false']);  // Expected Output: Luggage tax: 0.00
luggageTax([10, 4, 5, 'true']);  // Expected Output: Luggage tax: 10.00
luggageTax([5, 4, 3, 'true']);  // Expected Output: Luggage tax: 0.00
luggageTax([5, 7, 7, 'false']);  // Expected Output: Luggage tax: 100.00
