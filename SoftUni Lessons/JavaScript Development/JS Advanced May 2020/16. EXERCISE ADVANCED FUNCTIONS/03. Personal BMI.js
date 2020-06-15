function personalBMI(name, age, weight, height) {
    let bmi = (weight / (height ** 2)) * 10000;

    let state;
    if (bmi < 18.5) { state = 'underweight' }
    else if (bmi < 25) { state = 'normal' }
    else if (bmi < 30) { state = 'overweight' }
    else { state = 'obese'}

    let person = {
        name: name,
        personalInfo: { age: age, weight: Math.round(weight), height: Math.round(height) },
        BMI: Math.round(bmi),
        status: state};

    state === 'obese' ? person.recommendation = 'admission required' : 'or not :D';

    return person;
}

personalBMI('Peter', 29, 75, 182);  // Expected Output:
// { name: 'Peter',
//     personalInfo: {
//     age: 29,
//         weight: 75,
//         height: 182
// }
//     BMI: 23
//     status: 'normal' }

personalBMI('Honey Boo Boo', 9, 57, 137);  // Expected Output:
// { name: 'Honey Boo Boo', personalInfo: { age: 9, weight: 57, height: 137 }, BMI: 30, status: 'obese', recommendation: 'admission required' }