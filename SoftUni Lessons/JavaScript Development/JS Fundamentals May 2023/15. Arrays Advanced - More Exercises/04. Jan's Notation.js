function mask (params) {
    // MASK

    function simpleCalc (num1, num2, operator) {
    // MasK
    let result = {
        '*': (a, b) => {return a * b},
        '/': (a, b) => {return a / b},
        '+': (a, b) => {return a + b},
        '-': (a, b) => {return a - b}
    }[operator](num1, num2);

    return result;
    }

    let nums = []
    while (true) {
        if (params.length === 0) {
            if (nums.length > 1) {
                console.log('Error: too many operands!');
            } else {
                console.log(nums[0]);
            }
            break
        }

        let data = params.shift();

        if (Number.isInteger(data)) {
            // We have a number
            nums.push(Number(data));
        } else {
            // We have an operand
            if (nums.length < 2) {
                console.log("Error: not enough operands!");
                break;
            }
            let b = nums.pop();
            let a = nums.pop();
            let result = simpleCalc(a, b, data);
            nums.push(result);
        }
    }
}

mask([3,
4,
'+']);
// 7

console.log('-------------------------------------');

mask([5,
3,
4,
'*',
'-']);
// -7

console.log('-------------------------------------');

mask([7,
33,
8,
'-']);
// Error: too many operands!

console.log('-------------------------------------');

mask([15,
'/']);
// Error: not enough operands!



