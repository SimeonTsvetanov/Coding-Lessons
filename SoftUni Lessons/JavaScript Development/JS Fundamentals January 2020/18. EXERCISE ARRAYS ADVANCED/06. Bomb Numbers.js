function bombNumbers(sequence, data) {
    // Mask
    sequence.map(Number);
    let [special, power] = data.map(Number);
    for (let index = 0; index < sequence.length; index += 1) {
        if (sequence[index] === special) {
            let left = index - 1;
            let right = index + 1;
            for (let time = 1; time <= power; time ++) {
                delete sequence[left];
                delete sequence[right];
                left -= 1;
                right += 1;
            }
            delete sequence[sequence.indexOf(special)];
        }
    }

    let sum = sequence.reduce((a ,b) => a + b, 0);
    console.log(sum);
}

bombNumbers([1, 2, 2, 4, 2, 2, 2, 9], [4, 2]);
// Should return: 12

bombNumbers([1, 4, 4, 2, 8, 9, 1], [9, 3]);
// Should return: 5

bombNumbers([1, 1, 2, 1, 1, 1, 2, 1, 1, 1],
    [2, 1]
);
// Should return: 4