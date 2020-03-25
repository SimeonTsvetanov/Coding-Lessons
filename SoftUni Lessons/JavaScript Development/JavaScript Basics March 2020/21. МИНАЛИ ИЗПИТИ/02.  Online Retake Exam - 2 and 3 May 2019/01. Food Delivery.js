function foodDelivery(params) {
    let priceChickenMenus = Number(params.shift()) * 10.35;
    let priceFishMenus = Number(params.shift()) * 12.40;
    let priceVegeterianMenus = Number(params.shift()) * 8.15;

    let total = ((priceChickenMenus + priceFishMenus + priceVegeterianMenus) * 1.2) + 2.5;
    console.log(`Total: ${total.toFixed(2)}`);
}

foodDelivery(['2', '4', '3']);  // Expected Output: Total: 116.20
foodDelivery(['10', '0', '6']);  // Expected Output: Total: 185.38
foodDelivery(['1', '1', '1']);  // Expected Output: Total: 39.58