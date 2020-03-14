// There are two ways to test the task in Judge
// This is the new way:
function forecast(weather) {
    if (weather == "sunny") {
        console.log("It's warm outside!")
    }
    else {
        console.log("It's cold outside!")
    }
}
forecast("sunny"); // Expected Output: It's warm outside!
forecast("cloudy"); // Expected Output: It's cold outside!
forecast("snowy"); // Expected Output: It's cold outside!


// -----------------------------------------------------------------------------------//
// Old way of reading the input:
function forecastOld(input) {
    let weather = input.shift();
    if (weather == "sunny") {
        console.log("It's warm outside!")
    }
    else {
        console.log("It's cold outside!")
    }
}

forecastOld(["sunny"]); // Expected Output: It's warm outside!
forecastOld(["cloudy"]); // Expected Output: It's cold outside!
forecastOld(["snowy"]); // Expected Output: It's cold outside!
