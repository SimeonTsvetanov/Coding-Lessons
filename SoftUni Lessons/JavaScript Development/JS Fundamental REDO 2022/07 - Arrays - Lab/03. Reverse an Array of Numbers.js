function reverseArrayOfNumbers (count, numbers) {
    // MasK
    let newArray = numbers.slice(0, count)
    console.log(newArray.reverse().join(' '));
}

reverseArrayOfNumbers(3, [10, 20, 30, 40, 50]);