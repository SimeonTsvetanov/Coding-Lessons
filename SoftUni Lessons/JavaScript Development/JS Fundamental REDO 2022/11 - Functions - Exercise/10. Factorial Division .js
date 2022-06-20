function factorialDivision (a, b) {
    // MasK
    function factorial(num){
        return num === 1 ? 1 : num * factorial(num - 1)
    }

    console.log((factorial(a) / factorial(b)).toFixed(2));
}

factorialDivision(5, 2);