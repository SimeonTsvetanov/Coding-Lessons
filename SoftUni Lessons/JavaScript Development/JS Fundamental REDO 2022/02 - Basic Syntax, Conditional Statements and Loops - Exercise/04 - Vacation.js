function vacation(group_count, group_type, day) {
    let price_one = {
        'Students': {'Friday': 8.45, 'Saturday': 9.80, 'Sunday': 10.46},
        'Business': {'Friday': 10.90, 'Saturday': 15.60, 'Sunday': 16},
        'Regular': {'Friday': 15, 'Saturday': 20, 'Sunday': 22.50}
    }[group_type][day];

    let price = price_one * group_count;

    group_type === 'Students' && group_count >= 30 ? price *= 0.85 : 'pass';
    group_type === 'Business' && group_count >= 100 ? price -= (price_one * 10) : 'pass';
    group_type === 'Regular' && group_count >= 10 && group_count <= 20 ? price *= 0.95 : 'pass';

    console.log(`Total price: ${price.toFixed(2)}`);
}


vacation(30,
    "Students",
    "Sunday"
);

vacation(40,
    "Regular",
    "Saturday"
);
