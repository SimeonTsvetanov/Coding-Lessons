function evenOrOddPositions(params) {
    times = Number(params.shift());

    let oddSum = 0;
    let oddMin = [Number.MAX_SAFE_INTEGER, 'No'];
    let oddMax = [Number.MIN_SAFE_INTEGER, 'No']; 
    let evenSum = 0; 
    let evenMin = [Number.MAX_SAFE_INTEGER, 'No'];
    let evenMax = [Number.MIN_SAFE_INTEGER, 'No'];

    for(let time = 1; time <= times; time++) {
        let number = Number(params.shift());
        if (time % 2 != 0) {
            // We will ented the OddS:
            oddSum += number;
            if (number <= oddMin[0]) {oddMin[0] = number; oddMin[1] = 'Yes';}
            if (number >= oddMax[0]) {oddMax[0] = number; oddMax[1] = 'Yes';}
        } else {
            // We will ented the Evens:
            evenSum += number;
            if (number <= evenMin[0]) {evenMin[0] = number; evenMin[1] = 'Yes';}
            if (number >= evenMax[0]) {evenMax[0] = number; evenMax[1] = 'Yes';}
        }
    }

    console.log(`OddSum=${oddSum.toFixed(2)},`);
    if (oddMin[1] == 'No') {console.log(`OddMin=${oddMin[1]},`);}
    else {console.log(`OddMin=${oddMin[0].toFixed(2)},`);}
    if (oddMax[1] == 'No') {console.log(`OddMax=${oddMax[1]},`);}
    else {console.log(`OddMax=${oddMax[0].toFixed(2)},`);}

    console.log(`EvenSum=${evenSum.toFixed(2)},`);
    if (evenMin[1] == 'No') {console.log(`EvenMin=${evenMin[1]},`);}
    else {console.log(`EvenMin=${evenMin[0].toFixed(2)},`);}
    if (evenMax[1] == 'No') {console.log(`EvenMax=${evenMax[1]}`);}
    else {console.log(`EvenMax=${evenMax[0].toFixed(2)}`);}
    
}

evenOrOddPositions([6, 2, 3, 5, 4, 2, 1]);  // Expected Output:
// OddSum=9.00,
// OddMin=2.00, 
// OddMax=5.00, 
// EvenSum=8.00, 
// EvenMin=1.00,
// EvenMax=4.00

evenOrOddPositions([2, 1.5, -2.5]);  // Expected Output:
// OddSum=1.50, 
// OddMin=1.50, 
// OddMax=1.50, 
// EvenSum=-2.50, 
// EvenMin=-2.50, 
// EvenMax=-2.50