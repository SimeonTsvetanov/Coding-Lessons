function amazingNumbers(number) {
    let a = number.toString().split('').map(Number).reduce((a, b) => a + b).toString().split('').map(Number);
    a.includes(9) ? console.log(`${number} Amazing? True`) : console.log(`${number} Amazing? False`);
}

amazingNumbers(1233);
