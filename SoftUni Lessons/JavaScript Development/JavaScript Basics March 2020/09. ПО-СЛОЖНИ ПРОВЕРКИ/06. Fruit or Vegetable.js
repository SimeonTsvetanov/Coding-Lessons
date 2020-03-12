function fruitOrVegetable(input) {
    let fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'];
    let vegetables = ['tomato', 'cucumber', 'pepper', 'carrot'];

    let food = input.shift();

    if (fruits.includes(food)) {
        console.log("fruit");
    } else if (vegetables.includes(food)) {
        console.log("vegetable");
    } else {
        console.log("unknown");
    }
}

fruitOrVegetable(['banana']);  //Expected Output: fruit
fruitOrVegetable(['apple']);  //Expected Output: fruit
fruitOrVegetable(['tomato']);  //Expected Output: vegetable
fruitOrVegetable(['water']);  //Expected Output: unknown
