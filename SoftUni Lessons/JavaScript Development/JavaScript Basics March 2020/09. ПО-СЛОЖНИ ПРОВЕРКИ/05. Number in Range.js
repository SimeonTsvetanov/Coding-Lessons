function numberInRange(input) {
    number = Number(input.shift());

    if (number >= -100 && number <= 100 && number != 0) {
        console.log("Yes");
    } else {
        console.log("No")
    }
}

numberInRange(["-25"]) // Expected Output: Yes
numberInRange(["0"]) // Expected Output: No
numberInRange(["25"]) // Expected Output: Yes
