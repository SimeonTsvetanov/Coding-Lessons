function magicSum (nums, searchedSum) {
    // MasK
    for (let i = 0; i < nums.length; i++) {
        let a = nums[i];

        for (let j = i + 1; j < nums.length; j++) {
            let b = nums[j];

            a + b === searchedSum ? console.log(`${a} ${b}`) : 'continue';
        }
    }
}

magicSum ([1, 7, 6, 2, 19, 23],
    8
);

// 1 7
// 6 2


magicSum([14, 20, 60, 13, 7, 19, 8],
    27
)

// 14 13
// 20 7
// 19 8

magicSum([1, 2, 3, 4, 5, 6],
    6
)

// 1 5
// 2 4
