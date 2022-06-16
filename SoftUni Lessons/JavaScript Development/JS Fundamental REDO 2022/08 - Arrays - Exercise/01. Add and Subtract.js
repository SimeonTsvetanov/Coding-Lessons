function addAndSubtract (arr) {
    // MasK
    let modified = []
    arr.forEach((num, index) => {
       num % 2 === 0 ? modified.push(num + index) : modified.push(num - index);
    });

    const sumOriginal = arr.reduce((acc, curr) => acc + curr);
    const sumModified = modified.reduce((acc, curr) => acc + curr);

    console.log(modified);
    console.log(sumOriginal);
    console.log(sumModified);
}

addAndSubtract([5, 15, 23, 56, 35]);