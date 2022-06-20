function jansNotation (notations) {
    // MasK

    let nums = [];

    let calculator = {
        '+' : (a, b) => {return a + b},
        '-' : (a, b) => {return a - b},
        '*' : (a, b) => {return a * b},
        '/' : (a, b) => {return a / b}
    };

    for (const notation of notations) {
        if (!isNaN(notation)) {
            // if the instruction is a number, save it:
            nums.push(notation);
        } else {
            // otherwise, the instruction is an arithmetic operator (+-*/):
            if (nums.length > 1) {
                let b = nums.pop();
                let a = nums.pop();

                // Do the Operation:
                let result = calculator[notation](a, b);
                nums.push(result);
            } else {
                return console.log('Error: not enough operands!');
            }

        }
    }

    nums.length > 1 ? console.log(`Error: too many operands!`) : console.log(nums[0]);
}

jansNotation([3,
    4,
    '+']
);

// 7

jansNotation([5,
    3,
    4,
    '*',
    '-']
);

// -7

jansNotation([7,
    33,
    8,
    '-']
);

// Error: too many operands!

jansNotation([15,
    '/']
);

// Error: not enough operands!