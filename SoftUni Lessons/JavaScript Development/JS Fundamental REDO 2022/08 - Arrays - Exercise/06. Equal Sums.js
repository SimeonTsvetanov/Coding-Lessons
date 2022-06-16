function equalSums (arr) {
    // MasK
    let result = 0;

    arr.forEach((element, index) => {
        let left = arr.slice(0, index).reduce((a, b) => a + b, 0);
        let right = arr.slice(index + 1, arr.length).reduce((a, b) => a + b, 0);
        left === right ? result = index : 'continue';
    });

    if (arr.length <= 1) {
        console.log(0);
    } else if (result === 0) {
        console.log('no');
    } else {
        console.log(result);
    }
}

equalSums([1, 2, 3, 3])
equalSums([1, 2]);
equalSums([1])
