function sumFirstAndLastArrayElements(input) {
    // Mask
    // console.log(Number(input.shift()) + Number(input.pop()));
    console.log(Number(input[0]) + Number(input[input.length - 1]));
}

sumFirstAndLastArrayElements(['20', '30', '40']);  // Should return: 60

sumFirstAndLastArrayElements(['10', '17', '22', '33']);  // Should return: 43