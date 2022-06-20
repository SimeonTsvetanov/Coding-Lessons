function addAndSubtract (a, b, c) {
    // MasK
    let sum = (num1, num2) => {return num1 + num2};
    let subtract = (num1, num2) => {return num1 - num2};
    console.log(subtract(sum(a, b), c));
}

addAndSubtract(23, 6, 10);  // 19