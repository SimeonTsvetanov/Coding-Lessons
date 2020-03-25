function poolDay(params) {
    let people = Number(params.shift());    
    let entry = Number(params.shift());    
    let bed = Number(params.shift());    
    let umbrella = Number(params.shift());

    let priceEntry = people * entry;
    let priceBeds = Math.ceil(people * 0.75) * bed;
    let priceUmbrella = Math.ceil(people / 2) * umbrella;

    let total = priceEntry + priceBeds + priceUmbrella;
    
    console.log(`${total.toFixed(2)} lv.`);
}


poolDay(['21', '5.50', '4.40', '6.20']) // Expected  Output: 254.10 lv.
poolDay(['50', '6', '8', '4']) // Expected  Output: 704.00 lv.
poolDay(['100', '8', '6', '4']) // Expected  Output: 1450.00 lv.
