function basketballEquipement(params) {
    let price = Number(params.shift());
    let shoes = price * 0.6;
    let clothes = shoes * 0.8;
    let ball = clothes * 0.25;
    let accessories = ball * 0.2;
    
    let total = price + shoes + clothes + ball + accessories;

    console.log(total.toFixed(2));
}

basketballEquipement(['320']);  // Expected Output: 711.68
basketballEquipement(['550']);  // Expected Output: 1223.20
basketballEquipement(['230']);  // Expected Output: 511.52
