//  Not included in final score
function calorieObject(input) {
    // Mask
    let foods = {};

    for (i = 0; i < input.length; i += 2) {
        foods[input[i]] = Number(input[i + 1]);
    }

    console.log(foods);
}

calorieObject(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']);  // Should return:
// { Yoghurt: 48, Rise: 138, Apple: 52 }

calorieObject(['Potato', '93', 'Skyr', '63', 'Cucumber', '18', 'Milk', '42']);  // Should return:
// { Potato: 93, Skyr: 63, Cucumber: 18, Milk: 42 }