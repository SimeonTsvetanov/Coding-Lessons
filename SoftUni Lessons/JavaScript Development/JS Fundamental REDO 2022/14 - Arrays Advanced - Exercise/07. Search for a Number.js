function searchForANumber (nums, data) {
    // MasK
    const [take, del, num] = data;
    let result = nums.slice(0, take).splice(del);

    console.log(`Number ${num} occurs ${result.filter(i => i === num).length} times.`);
}

searchForANumber([5, 2, 3, 4, 1, 6],
    [5, 2, 3]
);

// Number 3 occurs 1 times.