function mask (num) {
    // MASK
    let even_sum = String(num)  // Format it String.
        .split('')  // Split the string 123 to a list ['1', '2', '3'].
        .map(Number)   // Now make the numbers in the list into numbers [1, 2, 3].
        .filter(a => a % 2 == 0)  // Filter only the Even ones.
        .reduce((a, b) => a + b, 0);  // Sum the list.

    let odd_sum = String(num)
        .split('')
        .map(Number)
        .filter(a => a % 2 != 0)
        .reduce((a, b) => a + b, 0);

    console.log(`Odd sum = ${odd_sum}, Even sum = ${even_sum}`);
}


mask(1000435);
// Odd sum = 9, Even sum = 4

mask(3495892137259234);
// Odd sum = 54, Even sum = 22
