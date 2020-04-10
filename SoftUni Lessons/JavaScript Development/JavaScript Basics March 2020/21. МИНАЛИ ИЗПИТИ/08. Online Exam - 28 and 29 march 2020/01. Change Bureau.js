function changeBureau(input) {
    // Mask
    let bitcons = Number(input.shift()) * 1168;  // yeah, right! morle liklly to be 10 times that.
    let yuans = (Number(input.shift()) * 0.15) * 1.76;
    let commision = Number(input.shift());
    let total = ((bitcons + yuans) / 1.95) * ((100 - commision) / 100);

    console.log(total.toFixed(2));
}

changeBureau([1, 5, 5]);  // Should return:
// 569.67

changeBureau([20, 5678, 2.4]);  // Should return:
// 12442.24