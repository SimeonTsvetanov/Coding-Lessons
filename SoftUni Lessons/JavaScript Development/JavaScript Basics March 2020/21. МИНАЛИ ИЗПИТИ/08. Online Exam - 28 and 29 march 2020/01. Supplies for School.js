function suppliesForSchool(input) {
    // Mask
    let pens = Number(input.shift() * 5.80);
    let markers = Number(input.shift()) * 7.20;
    let chemical = Number(input.shift()) * 1.20;
    let discount = Number(input.shift());

    let total = (pens + markers + chemical) * ((100 - discount) /100);
    console.log(total.toFixed(3));
}

suppliesForSchool([2, 3, 2.5, 25]);  // Should return:
// 27.150

suppliesForSchool([4, 2, 5, 13]);  // Should return:
// 37.932