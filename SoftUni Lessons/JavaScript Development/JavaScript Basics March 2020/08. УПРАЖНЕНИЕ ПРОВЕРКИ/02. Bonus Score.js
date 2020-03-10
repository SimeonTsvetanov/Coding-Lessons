function bonusScore(input) {
    let number = Number(input.shift());
    let bonus = 0;

    if (number <= 100) {
        bonus += 5;
    } else if (number <= 1000) {
        bonus += number * 0.2;
    } else if (number > 1000) {
        bonus += number * 0.1;
    }

    if (number % 2 === 0) {
        bonus += 1;
    } else if ((number % 10) === 5) {
        bonus += 2;
    }
    
    console.log(bonus)
    console.log(number + bonus)
}

bonusScore(["20"])  // Expected Output: 6/26
bonusScore(["175"])  // Expected Output: 37/212
bonusScore(["2703"])  // Expected Output: 270.3/2973.3
bonusScore(["15875"])  // Expected Output: 1589.5/ 17464.5
