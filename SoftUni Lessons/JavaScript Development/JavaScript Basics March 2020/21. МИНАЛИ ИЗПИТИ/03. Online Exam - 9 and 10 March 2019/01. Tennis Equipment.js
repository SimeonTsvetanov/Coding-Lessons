function tennisEquipment(params) {
    let priceRocket = Number(params.shift());
    let countRockets = Number(params.shift());
    let countShoes = Number(params.shift());

    let total_rockets = priceRocket * countRockets;
    let total_kicks = (priceRocket / 6) * countShoes;
    let total_extra = (total_rockets + total_kicks) * 0.2;
    let total = total_rockets + total_kicks + total_extra;

    let own = total / 8;
    let sponsor = total * 7 / 8;

    console.log(`Price to be paid by Djokovic ${Math.floor(own)}`)
    console.log(`Price to be paid by sponsors ${Math.ceil(sponsor)}`)
}

tennisEquipment(['850', '4', '2']);  // Expected output:
// Price to be paid by Djokovic 552
// Price to be paid by sponsors 3868

tennisEquipment(['1000', '3', '1']);  // Expected output:
// Price to be paid by Djokovic 475
// Price to be paid by sponsors 3325

tennisEquipment(['386', '7', '4']);  // Expected output:
// Price to be paid by Djokovic 443
// Price to be paid by sponsors 3108
