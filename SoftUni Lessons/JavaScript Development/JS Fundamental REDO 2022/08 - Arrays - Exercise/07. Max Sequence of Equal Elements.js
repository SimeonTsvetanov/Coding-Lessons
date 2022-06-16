function maxSequenceOfEqualElements (elements) {
    // MasK
    let maxSequence = [];

    elements.forEach((element, index) => {
        let currentSequence = [];
        for (const e of elements.slice(index, elements.length)) {
            if (e === element) {
                currentSequence.push(element);
            } else {
                break;
            }
            currentSequence.length > maxSequence.length ? maxSequence = currentSequence : 'pass';
        }
    });

    console.log(maxSequence.join(' '));
}

maxSequenceOfEqualElements([2, 1, 1, 2, 3, 3, 2, 2, 2, 1]);  // 2 2 2
maxSequenceOfEqualElements([1, 1, 1, 2, 3, 1, 3, 3]);  // 1 1 1
maxSequenceOfEqualElements([4, 4, 4, 4]);  // 4 4 4 4
maxSequenceOfEqualElements([0, 1, 1, 5, 2, 2, 6, 3, 3]);  // 1 1