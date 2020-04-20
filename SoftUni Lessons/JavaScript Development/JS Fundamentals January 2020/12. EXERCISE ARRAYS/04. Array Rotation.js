function arrayRotation(array, times) {
    // Mask
    for (let time = 1; time <= times; time += 1) {
        array.push(array.shift());
    }
    console.log(array.join(' '));
}

arrayRotation([51, 47, 32, 61, 21], 2);
// Should return: 32 61 21 51 47

arrayRotation([32, 21, 61, 1], 4);
// Should return: 32 21 61 1
