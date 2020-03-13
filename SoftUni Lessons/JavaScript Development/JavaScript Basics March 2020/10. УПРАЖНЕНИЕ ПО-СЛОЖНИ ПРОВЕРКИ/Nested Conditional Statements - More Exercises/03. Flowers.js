function flowersShop(input) {
    let countChrysanthemums = Number(input.shift());
    let countRoses = Number(input.shift());
    let countTulips = Number(input.shift());
    let season = input.shift();  // Spring, Summer, Аutumn, Winter
    let hollyday = input.shift();  // Y or N

    let prices = {
        "Chrysanthemums": {"Spring": 2.00, "Summer": 2.00, "Autumn": 3.75, "Winter": 3.75},
        "Roses": {"Spring": 4.10, "Summer": 4.10, "Autumn": 4.50, "Winter": 4.50},
        "Tulips": {"Spring": 2.50, "Summer": 2.50, "Autumn": 4.15, "Winter": 4.15},
    };
    
    let priceChrysanthemums = prices["Chrysanthemums"][season] * countChrysanthemums;
    let priceRoses = prices["Roses"][season] * countRoses;
    let priceTulips = prices["Tulips"][season] * countTulips;

    let price = priceChrysanthemums + priceRoses + priceTulips;

    if (hollyday == "Y") {price *= 1.15;}
    if (countTulips > 7 && season == "Spring") {price *= 0.95;}
    if (countRoses >= 10 && season == "Winter") {price *= 0.9;}
    if (countChrysanthemums + countRoses + countTulips > 20) {price *= 0.8;}

    console.log((price + 2).toFixed(2))  // Adding 2 for the arrangement :D
}

flowersShop(['2', '4', '8', 'Spring', 'Y']);  // Expected Output: 46.14
flowersShop(['3', '10', '9', 'Winter', 'N']);  // Expected Output: 69.39
flowersShop(['10', '10', '10', 'Autumn', 'N']);  // Expected Output: 101.20
