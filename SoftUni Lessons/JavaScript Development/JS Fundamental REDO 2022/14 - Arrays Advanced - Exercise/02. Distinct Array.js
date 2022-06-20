function distinctArray (nums) {
    // MasK
    console.log(...new Set(nums));
}

distinctArray([1, 2, 3, 4]);  // 1 2 3 4
distinctArray([7, 8, 9, 7, 2, 3, 4, 1, 2]);  // 7 8 9 2 3 4 1