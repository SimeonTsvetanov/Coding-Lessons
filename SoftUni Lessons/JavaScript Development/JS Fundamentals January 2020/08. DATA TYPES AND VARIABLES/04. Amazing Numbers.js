function amazingNumbers(num) {
    // Mask
    num = num.toString();
    let total = 0;

    for (let digit of num) {
        total += Number(digit);
    }

    let amazing = total.toString().includes('9') ? 'True' : 'False';
    console.log(`${num} Amazing? ${amazing}`);
}


amazingNumbers(1233);  // Should return: 1233 Amazing? True

amazingNumbers(999);  // Should return: 999 Amazing? False
