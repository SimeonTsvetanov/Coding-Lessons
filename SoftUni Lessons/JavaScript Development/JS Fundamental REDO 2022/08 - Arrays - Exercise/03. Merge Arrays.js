function mergeArrays (arr1, arr2) {
    // MasK
    let modified = [];

    arr1.forEach((num, index) => {
        index % 2 === 0
            ? modified.push(Number(arr1[index]) + Number(arr2[index]))
            : modified.push(arr1[index].toString() + arr2[index].toString());
    });

    console.log(modified.join(' - '));
}

mergeArrays(['5', '15', '23', '56', '35'],
    ['17', '22', '87', '36', '11']
);