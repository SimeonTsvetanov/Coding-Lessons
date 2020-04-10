function foodForPets(input) {
    // Mask
    days = Number(input.shift());
    food = Number(input.shift());

    let eatenFood = 0;
    let dogFood = 0;
    let catFood = 0;
    let biscuits = 0;

    for (let day = 1; day <= days; day += 1) {
        let dog = Number(input.shift());
        let cat = Number(input.shift());

        eatenFood += dog + cat;
        dogFood += dog;
        catFood += cat;

        if (day % 3 == 0) {
            biscuits += ((dog + cat) * 0.1);
        }
    }
    
    console.log(`Total eaten biscuits: ${Math.round(biscuits)}gr.`);
    console.log(`${(eatenFood / food * 100).toFixed(2)}% of the food has been eaten.`);
    console.log(`${(dogFood / eatenFood * 100).toFixed(2)}% eaten from the dog.`);
    console.log(`${(catFood / eatenFood * 100).toFixed(2)}% eaten from the cat.`);
}

foodForPets([3, 1000, 300, 20, 100, 30, 110, 40]);  // Should return:
// Total eaten biscuits: 15gr.
// 60.00% of the food has been eaten.
// 85.00% eaten from the dog.
// 15.00% eaten from the cat.

foodForPets([3, 500, 100, 30, 110, 25, 120, 35]);  // Should return:
// Total eaten biscuits: 16gr.
// 84.00% of the food has been eaten.
// 78.57% eaten from the dog.
// 21.43% eaten from the cat.
