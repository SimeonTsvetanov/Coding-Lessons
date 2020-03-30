function equalPairs(input) {
    // Mask: This task was F*****g sick. just too much thinking :D
    let times = Number(input.shift())

    let all = true;
    let diff = Number.MIN_SAFE_INTEGER;
    let last = (Number(input.shift()) + Number(input.shift()));

    for (let i = 1; i < times; i++) {
        let num = (Number(input.shift()) + Number(input.shift()));
        if (num != last) {
            all = false;
            curent = Math.abs(num - last);
            last = num;
            if (curent > diff) {diff = curent;}
        }
    }

    if (all) {
        console.log(`Yes, value=${last}`);
    } else {
        console.log(`No, maxdiff=${diff}`);
    }
}

equalPairs([3, 1, 2, 0, 3, 4, -1]);  // Should return: Yes, value=3

equalPairs([2, 1, 2, 2, 2]);  // Should return: No, maxdiff=1