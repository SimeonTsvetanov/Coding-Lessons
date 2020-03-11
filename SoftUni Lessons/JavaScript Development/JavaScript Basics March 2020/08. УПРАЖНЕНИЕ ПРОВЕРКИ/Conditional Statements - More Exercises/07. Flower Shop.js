function flowerShop(input) {
    let magnolias = Number(input.shift()) * 3.25;  // манголии - magnolias - 3.25
    let hyacinths = Number(input.shift()) * 4;  // зюмбюли - hyacinths - 4
    let roses = Number(input.shift()) * 3.50;  // рози - roses - 3.50
    let cactuses = Number(input.shift()) * 8;  // кактуси - cactuses - 8
    let giftPrice = Number(input.shift());

    let total = (magnolias + hyacinths + roses + cactuses) * 0.95;  // yeah VAT sucks!!!
    
    if (total >= giftPrice) {
        console.log(`She is left with ${Math.floor(total - giftPrice)} leva.`);
    } else {
        console.log(`She will have to borrow ${Math.ceil(giftPrice - total)} leva.`)
    }
}

flowerShop(['2', '3', '5', '1', '50']);  // Expected Output: She will have to borrow 9 leva.
flowerShop(['15', '7', '5', '10', '100']);  // Expected Output: She is left with 65 leva.
