function equalArrays(one, two) {
    // Mask
    let sum = 0;
    let equal = true;

    for (let index = 0; index < one.length; index++) {
        if (Number(one[index]) === Number(two[index])) {
            sum += Number(one[index]);
        } else {
            equal = false;
            console.log(`Arrays are not identical. Found difference at ${index} index`);
            break;
        }
    }

    if (equal) {
        console.log(`Arrays are identical. Sum: ${sum}`);
    }
}


equalArrays(['10','20','30'], ['10','20','30', '40']);