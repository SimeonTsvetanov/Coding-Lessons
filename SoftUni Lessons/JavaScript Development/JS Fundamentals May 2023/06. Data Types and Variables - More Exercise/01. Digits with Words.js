function mask (params) {
    // MASK
    const num = params;
    const numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    };

    console.log(numbers[num]);
}

mask('nine');
// 9

mask('two');
// 2
