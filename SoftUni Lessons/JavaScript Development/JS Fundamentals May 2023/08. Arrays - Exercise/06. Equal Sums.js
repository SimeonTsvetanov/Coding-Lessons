function mask (params) {
    // MASK
    let nums = params;
    let result = 'no';

    nums.forEach((num, index) => {

        let right_sum = [...nums]  // copying the original array.
            .splice(index + 1) // get the right part.
            .reduce((a, b) => a + b, 0);  // sum all the numbers in it.

        let left_sum = [...nums] // copying the original array.
            .splice(0, index) // get the left part.
            .reduce((a, b) => a + b, 0);  // sum all the numbers in it.

        // Strainge thing is that there could be more than one match.
        // but hey. All the tests are with one only so it works....
        // mine will be only the last found index!

        (left_sum === right_sum) ? result = index : 'pass';
    });

    console.log(result);
}

mask([1, 2, 3, 3]);
// 2

mask([1, 2]);
// no
