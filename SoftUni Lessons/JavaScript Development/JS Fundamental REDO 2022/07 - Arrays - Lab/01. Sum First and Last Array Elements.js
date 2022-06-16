function sumFirstAndLastElements (arr) {
    // MasK
    let sum = arr.shift() + arr.pop();
    console.log(sum);
}

sumFirstAndLastElements([20, 30, 40]);
