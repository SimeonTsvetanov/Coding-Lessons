function lettersSum(productName, control, buddget) {
    // Mask
    let sum = 0;

    for (const letter of productName) {
        if ("aeiouy".includes(letter)) {
            sum += 3;
        } else {
            sum += 1;
        }
    }

    sum *= control;
    
    if (buddget < sum) {
        console.log(`Cannot buy ${productName}. Product value: ${sum.toFixed(2)}`);
    } else {
        console.log(`${productName} bought. Money left: ${(buddget - sum).toFixed(2)}`);
    }
}

lettersSum('apple', 2, 20);  // Should return:
// apple bought. Money left: 2.00

lettersSum('milk', 1.4, 8);  // Should return:
// Cannot buy milk. Product value: 8.40