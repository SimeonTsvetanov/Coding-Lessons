// Short link bru: https://bit.ly/3bwnN3O

function fruitShop(...input) {
    let fruit = input.shift();
    let day = input.shift();
    let valume = Number(input.shift());
    
    let weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
    let weekends = ['Saturday', 'Sunday'];

    weekPrices = {
        'banana': 2.50, 
        'apple': 1.20, 
        'orange': 0.85, 
        'grapefruit': 1.45, 
        'kiwi': 2.70, 
        'pineapple': 5.50, 
        'grapes': 3.85
    };

    weekendPrices = {
        'banana': 2.70, 
        'apple': 1.25, 
        'orange': 0.90, 
        'grapefruit': 1.60, 
        'kiwi': 3.00, 
        'pineapple': 5.60, 
        'grapes': 4.20
    };

    let price = 0

    if (weekDays.includes(day)) {
        price = weekPrices[fruit] * valume;
    } else if (weekends.includes(day)) {
        price = weekendPrices[fruit] * valume;
    }

    if (price) {
        console.log(price.toFixed(2));
    } else {
        console.log('error');
    }
}

fruitShop(['apple', 'Tuesday', '2']);  // Expected Output: 2.40
fruitShop(['orange', 'Sunday', '3']);  // Expected Output: 2.70
fruitShop(['kiwi', 'Monday', '2.5']);  // Expected Output: 6.75
fruitShop(['grapes', 'Saturday', '0.5']);  // Expected Output: 2.10
fruitShop(['tomato', 'Monday', '0.5']);  // Expected Output: error
