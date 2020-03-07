function usdToBgn(input) {
    let usd = Number(input.shift());
    let bgn = (usd * 1.79549).toFixed(2);
    console.log(bgn);
}

usdToBgn([20]);
usdToBgn([100]);
usdToBgn([12.5]);
