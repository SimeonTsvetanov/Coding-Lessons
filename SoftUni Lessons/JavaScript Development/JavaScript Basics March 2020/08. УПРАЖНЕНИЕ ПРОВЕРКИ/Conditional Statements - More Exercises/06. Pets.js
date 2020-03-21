function pets(...input) {
    let days = Number(input.shift());
    let leftFood = Number(input.shift());
    let dogDayFood = Number(input.shift()) * days;
    let catDayFood = Number(input.shift()) * days;
    let turtleDayFood = (Number(input.shift()) * 0.001) * days;

    let neededFood = dogDayFood + catDayFood + turtleDayFood;
    if (neededFood <= leftFood) {
        console.log(`${Math.floor(leftFood - neededFood)} kilos of food left.`);
    } else {
        console.log(`${Math.ceil(neededFood - leftFood)} more kilos of food are needed.`);
    }
}

pets(['2', '10', '1', '1', '1200'])  // Expected Output: 3 kilos of food left.
pets(['5', '10', '2.1', '0.8', '321'])  // Expected Output: 7 more kilos of food are needed.
