function rotateArray(array = []) {
    // Mask: Optimisation was required...
    let times = Number(array.pop())

    for (let time = 1; time <= times; time++) {
        array.unshift(array.pop());
    }

    console.log(array.join(' '));
}

rotateArray(['1', '2', '3', '4', '2']);  // 3 4 1 2