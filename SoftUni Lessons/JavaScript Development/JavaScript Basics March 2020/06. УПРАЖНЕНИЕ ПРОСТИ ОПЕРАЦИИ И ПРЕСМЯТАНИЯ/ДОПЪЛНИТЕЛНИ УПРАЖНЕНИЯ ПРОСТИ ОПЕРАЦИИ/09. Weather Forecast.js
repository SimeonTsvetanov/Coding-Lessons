function forecast(input) {
    let weather = input.shift();
    if (weather == "sunny") {
        console.log("It's warm outside!")
    }
    else {
        console.log("It's cold outside!")
    }
}

forecast(["sunny"]); // Expected Output: It's warm outside!
forecast(["cloudy"]); // Expected Output: It's cold outside!
forecast(["snowy"]); // Expected Output: It's cold outside!
