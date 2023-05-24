function excellentResult(params) {
    let socre = Number(params[0]);
    (socre >= 5.5) ? console.log('Excellent!') : 'pass';
}

// excellentResult(["6"]);  // Excellent!
// excellentResult(["5"]);  // Няма изход
// excellentResult(["5.5"]);  // Excellent!
// excellentResult(["5.49"]);  // Няма изход

function greaterNumber(params) {
    let a = Number(params[0]);
    let b = Number(params[1]);

    (a > b) ? console.log(a) : console.log(b);
}

// greaterNumber(["5", "2"]);  // 5

function evenOrOdd(params) {
    let num = Number(params[0]);

    (num % 2 === 0) ? console.log('even') : console.log('odd');
}

// evenOrOdd(["5"]);  // odd
// evenOrOdd(["6"]);  // even

function passwordGuess(params) {
    (params[0] === "s3cr3t!P@ssw0rd") ? console.log('Welcome') : console.log('Wrong password!');
}

// passwordGuess(["s3cr3t!P@ssw0rd"]);  // Welcome
// passwordGuess(['asd'])  // Wrong password!

function numbers100To200(params) {
    let num = Number(params[0]);
 
    if (num < 100) {
        console.log("Less than 100");
    } else if (num >= 100 && num <= 200) {
        console.log("Between 100 and 200");
    } else {
        console.log("Greater than 200");
    }
}

// numbers100To200(["100"]);  // Between 100 and 200

function speedInfo(params) {
    let speed = Number(params[0]);

    if (speed <= 10) {console.log('slow');}
    else if (speed > 10 && speed <= 50) {console.log('average');}
    else if (speed > 50 && speed <= 150) {console.log('fast');}
    else if (speed > 150 && speed <= 1000) {console.log('ultra fast');}
    else {console.log('extremely fast');}
}

// speedInfo(['8']);  // Slow

function areaOfFigures(params) {

    const calculateArea = (form, a, b= 'a') => {
        if (form === 'square') {
            return (a * a);
        } else if (form === 'rectangle') {
            return (a * b);
        } else if (form === 'circle') {
            return (Math.PI * a * a);
        } else if (form === 'triangle') {
            return((a * b) / 2);
        }
    }

    console.log(calculateArea(params[0], Number(params[1]), Number(params[2])).toFixed(3));
}

// areaOfFigures(["square", "5"]);  // 25.000
// areaOfFigures(["rectangle", "7", "2.5"])  // 17.500
// areaOfFigures(["circle", "6"])  // 113.097
// areaOfFigures(["triangle", "4.5", "20"])  // 45.000
