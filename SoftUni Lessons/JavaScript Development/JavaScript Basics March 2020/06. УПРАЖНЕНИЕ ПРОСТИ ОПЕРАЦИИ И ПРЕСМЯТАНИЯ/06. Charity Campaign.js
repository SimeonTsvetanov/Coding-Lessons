// New way of reading the Input
function charity(days, cooks, cakes, waffles, pancakes) {
    let total = ((days * (cooks * ((cakes * 45) + (waffles * 5.80) + (pancakes * 3.20)))) * 0.875).toFixed(2);
    console.log(total);
}
charity(["20", "8", "14", "30", "16"]);  // Expected output: 119728.00
charity(["131", "5", "9", "33", "46"]);  // Expected output: 426175.75

//-----------------------------------------------------------------------------------
// Old way of reading the input:
function charityOld(input) {
    let days = Number(input.shift());
    let cooks = Number(input.shift());
    let cakes = Number(input.shift());
    let waffles = Number(input.shift());
    let pancakes = Number(input.shift());
    let total = ((days * (cooks * ((cakes * 45) + (waffles * 5.80) + (pancakes * 3.20)))) * 0.875).toFixed(2);
    console.log(total);
}
charityOld(["20", "8", "14", "30", "16"]);  // Expected output: 119728.00
charityOld(["131", "5", "9", "33", "46"]);  // Expected output: 426175.75
