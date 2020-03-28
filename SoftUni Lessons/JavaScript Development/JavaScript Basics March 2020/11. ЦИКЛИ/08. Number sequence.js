// I have two versions for this solution:

// Basic Version:
function numberSequenceONE(params) {
    let times = Number(params.shift());

    let maxNumber = Number.MIN_SAFE_INTEGER;
    let minNumber = Number.MAX_SAFE_INTEGER;

    for (i = 1; i <= times; i++) {
        let number = Number(params.shift());
        
        if (number > maxNumber) {
            maxNumber = number;
        }

        if (number < minNumber) {
            minNumber = number;
        }
    }

    console.log(`Max number: ${maxNumber}`);
    console.log(`Min number: ${minNumber}`);
}


// Advanced Version:
function numberSequenceTWO(params) {
    let times = Number(params.shift());

    let numbers = [];

    for (i = 1; i <= times; i++) {
        numbers.push(Number(params.shift()));
    }

    console.log(`Max number: ${Math.max.apply(null, numbers)}`);
    console.log(`Min number: ${Math.min.apply(null, numbers)}`);
}

numberSequenceONE([5, 10, 20, 304, 0, 50]);
