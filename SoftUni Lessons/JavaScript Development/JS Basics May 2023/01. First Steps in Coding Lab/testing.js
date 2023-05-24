function helloSoftUni() {
    console.log("Hello SoftUni");
}

// helloSoftUni();

function numsOneToTen() {
    [1,2,3,4,5,6,7,8,9,10].forEach(element => {
        console.log(element);
    });
}

// numsOneToTen();

function squareArea(input) {
    let side = Number(input);
    let area = side * side;
    console.log(area);
}

// squareArea('4');

function inchToCentimeter(inch) {
    let centimeter = Number(inch) * 2.54;
    console.log(centimeter);
}

// inchToCentimeter('2');

function greetingByName(params) {
    let name = params[0];
    console.log(`Hello, ${name}!`);
}

// greetingByName(['John']);

function concatenateData(params) {
    let firstName = params[0];
    let lastName = params[1];
    let age = params[2];
    let town = params[3];

    let data = `You are ${firstName} ${lastName}, a ${age}-years old person from ${town}.`;
    console.log(data);
}

// concatenateData(['John', 'Doe', 30, 'London']);

function projectCreation([name, projectsCount]) {
    let neededTime = Number(projectsCount) * 3;
    let result = `The architect ${name} will need ${neededTime} hours to complete ${projectsCount} project/s.`;
    console.log(result);
}

// projectCreation(["George ","4"]);

function petShop(params) {
    let dogFood = Number(params[0]) * 2.5;
    let catFood = Number(params[1]) * 4;

    let result = dogFood + catFood;
    console.log(`${result} lv.`);
}

// petShop(["5", "4"]);

function yardGreening(params) {
    let area = Number(params);
    let priceSquareMeter = 7.61;
    let price = area * priceSquareMeter;
    let discount = price * 0.18;
    let discountedPrice = price - discount;

    console.log(`The final price is: ${discountedPrice} lv.`);
    console.log(`The discount is: ${discount} lv.`);
}

yardGreening(["550"]);
// The final price is: 3432.11 lv.
// The discount is: 753.39 lv.
