function schoolCamp(input) {
    let season = input.shift();  // Winter, Spring or Summer
    let groupType = input.shift();  // boys, girls or mixed
    let studentsCount = Number(input.shift());
    let nightsCount = Number(input.shift());

    let data = {
        // How it works: Season: {groupType: [priceRoom, Sport]} // Dict. -> Dict. -> List :D
        'Winter': {'boys': [9.6, 'Judo'], 'girls': [9.6, 'Gymnastics'], 'mixed': [10, 'Ski']},
        'Spring': {'boys': [7.2, 'Tennis'], 'girls': [7.2, 'Athletics'], 'mixed': [9.5, 'Cycling']},
        'Summer': {'boys': [15, 'Football'], 'girls': [15, 'Volleyball'], 'mixed': [20, 'Swimming']}
    };

    let price = data[season][groupType][0] * studentsCount * nightsCount;
    let sport = data[season][groupType][1];

    if (studentsCount >= 50) {price *= 0.5}
    if (studentsCount >= 20 && studentsCount < 50) {price *= 0.85}
    if (studentsCount >= 10 && studentsCount < 20) {price *= 0.95}

    console.log(`${sport} ${price.toFixed(2)} lv.`);
}

schoolCamp(['Spring', 'girls', '20', '7']); // Expected Output: Athletics 856.80 lv.
schoolCamp(['Winter', 'mixed', '9', '15']);  // Expected Output: Ski 1350.00 lv.
schoolCamp(['Summer', 'boys', '60', '7']);  // Expected Output: Ski 3150.00 lv.
schoolCamp(['Spring', 'mixed', '17', '14']);  // Expected Output: Ski 2147.95 lv.
