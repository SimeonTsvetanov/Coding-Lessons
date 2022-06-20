function nonDecreasingSubset (array) {
    // MasK
    let maxNum = array[0];

    let result = [];

    array.forEach(n => {
       if (n >= maxNum) {
           maxNum = n;
           result.push(n)
       }
    });

    console.log(result.join(' '));
}

nonDecreasingSubset([ 1, 3, 8, 4, 10, 12, 3, 2, 24]);  // 1 3 8 10 12 24
nonDecreasingSubset([ 1, 2, 3, 4, 4]);  // 1 2 3 4