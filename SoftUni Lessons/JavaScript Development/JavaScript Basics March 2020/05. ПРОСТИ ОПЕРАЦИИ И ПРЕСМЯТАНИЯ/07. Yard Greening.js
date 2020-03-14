function yardGreening(sqareMeters) {
    let full_price = sqareMeters * 7.61;
    let discount = (full_price * 0.18).toFixed(2);
    let final_price = (full_price - discount).toFixed(2);
    console.log(`The final price is: ${final_price} lv.`);
    console.log(`The discount is: ${discount} lv.`);
}

yardGreening(540);
yardGreening(135);

