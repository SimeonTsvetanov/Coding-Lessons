function sumOfNumbers(params) {
    let sum = params.shift().split('').map(Number).reduce((a, b) => a + b, 0);
    console.log(`The sum of the digits is:${sum}`);
}

sumOfNumbers(["1234"])  // The sum of the digits is:10 
sumOfNumbers(["564891"])  // The sum of the digits is:33
