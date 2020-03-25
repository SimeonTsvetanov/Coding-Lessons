function movieProfit(params) {
    name = params.shift();
    days = Number(params.shift());
    count = Number(params.shift());
    price = Number(params.shift());
    percentage = Number(params.shift());

    let total = (days * (count * price)) - ((days * (count * price)) * percentage / 100);

    console.log(`The profit from the movie ${name} is ${total.toFixed(2)} lv.`);   
}


movieProfit(['The Programmer', '20', '500', '7.50', '7']);  // Expected output: 
// The profit from the movie The Programmer is 69750.00 lv.

movieProfit(['Python Basics', '40', '34785', '10.45', '14']);  // Expected output: 
// The profit from the movie Python Basics is 12504511.80 lv.

movieProfit(['The Jungle', '22', '20500', '9.37', '30']);  // Expected output: 
// The profit from the movie The Jungle is 2958109.00 lv.
