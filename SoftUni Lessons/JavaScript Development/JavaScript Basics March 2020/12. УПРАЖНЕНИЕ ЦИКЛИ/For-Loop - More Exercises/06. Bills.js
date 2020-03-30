function bills(input) {
    // Mask
    let months = Number(input.shift());

    let totalElectricity = 0;
    let totalWater = 0;
    let totalInternet = 0;
    let totalOther = 0;

    let average = 0;

    for (let i = 1; i <= months; i++) {
        let cEl = Number(input.shift());
        
        totalElectricity += cEl;
        totalWater += 20;
        totalInternet += 15;
        totalOther += (cEl + 35) * 1.2;
        average += cEl + 35 + ((cEl + 35) * 1.2);
    }

    console.log(`Electricity: ${totalElectricity.toFixed(2)} lv`);
    console.log(`Water: ${totalWater.toFixed(2)} lv`);
    console.log(`Internet: ${totalInternet.toFixed(2)} lv`);
    console.log(`Other: ${totalOther.toFixed(2)} lv`);
    console.log(`Average: ${(average / months).toFixed(2)} lv`);
}

bills([5, 68.63, 89.25, 132.53, 93.53, 63.22]);  // Should return:
// Electricity: 447.16 lv
// Water: 100.00 lv
// Internet: 75.00 lv
// Other: 746.59 lv
// Average: 273.75 lv

bills([8, 123.54, 231.54, 140.23, 100, 122.4, 430, 178.52, 64.2]);  // Should return:
// Electricity: 1390.43 lv
// Water: 160.00 lv
// Internet: 120.00 lv
// Other: 2004.52 lv
// Average: 459.37 lv
