function vacantion(count, type, day) {
    // Mask
    let prices = {
        'Students': {'Friday': 8.45, 'Saturday': 9.8, 'Sunday': 10.46},
        'Business': {'Friday': 10.90, 'Saturday': 15.60, 'Sunday': 16},
        'Regular': {'Friday': 15, 'Saturday': 20, 'Sunday': 22.50}
    };
    
    let price = prices[type][day];
    
    if (type == 'Students' && count >= 30) {
        price *= 0.85;
    } else if (type == 'Business' && count >= 100) {
        count -= 10;
    } else if (type == 'Regular' && (count >= 10 && count <= 20)) {
        price *= 0.95;
    }

    price *= count;

    console.log(`Total price: ${price.toFixed(2)}`);
}

vacantion(30, "Students", "Sunday");  // Should return:
// Total price: 266.73

vacantion(40, "Regular", "Saturday");  // Should return:
// Total price: 800.00