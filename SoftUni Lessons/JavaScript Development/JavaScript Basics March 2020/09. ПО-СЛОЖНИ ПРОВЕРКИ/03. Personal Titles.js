function personalTitles(input) {
    let age = Number(input.shift());
    let sex = input.shift();

    let title = '';

    if (sex === "m") {
        if (age >= 16) {
            title = "Mr.";
        } else {
            title = "Master";
        }
    } else {
        if (age >= 16) {
            title = "Ms.";
        } else {
            title = "Miss";
        }
    }

    console.log(title);
}

personalTitles(["12", "f"]);  // Expected Output: Miss
personalTitles(["17", "m"]);  // Expected Output: Mr.
personalTitles(["25", "f"]);  // Expected Output: Ms.
personalTitles(["13.5", "m"]);  // Expected Output: Master
