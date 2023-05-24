function cleverLily(params) {
    let currentAge = Number(params.shift());
    let price = Number(params.shift());
    let priceToy = Number(params.shift());

    let savings = 0;
    let presentMoney = 10;

    for (let age = 1; age <= currentAge; age++) {
        if (age % 2 !== 0) {
            // TOY
            savings += priceToy;
        } else {
            // MONEY
            savings += presentMoney - 1;
            presentMoney += 10;
        }
    }

    (savings >= price) 
        ? console.log(`Yes! ${(savings - price).toFixed(2)}`)
        : console.log(`No! ${(price - savings).toFixed(2)}`);;
}

cleverLily(["10",
"170.00",
"6"]);
// Yes! 5.00

cleverLily(["21",
"1570.98",
"3"])
// No! 997.98