function celsiusToFahrenheit(input) {
    let celsius = Number(input.shift());
    let fahrenheit = ((celsius * 9 / 5) + 32).toFixed(2);
    console.log(fahrenheit); 
}

celsiusToFahrenheit([25]); // Expected putput: 77.00
celsiusToFahrenheit([0]); // Expected putput: 32.00
celsiusToFahrenheit([-5.5]); // Expected putput: 22.10
celsiusToFahrenheit([32.3]); // Expected putput: 90.14
