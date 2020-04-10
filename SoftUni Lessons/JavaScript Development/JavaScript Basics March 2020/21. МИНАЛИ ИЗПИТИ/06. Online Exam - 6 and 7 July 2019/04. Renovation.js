function renovation(input) {
    let height = Number(input.shift());
    let width = Number(input.shift());
    let otherAreas = (100 - Number(input.shift())) / 100;
    let total = Math.ceil((height * width * 4) * otherAreas);

    while('Tired or Done!') {
        let command = input.shift();
        if (command == 'Tired!') {
            // Pesho is lazy-ass
            console.log(`${total} quadratic m left.`);
            break
        }

        let liters = Number(command);

        total -= liters;

        if (total <= 0) {
            if (total < 0) {
                 console.log(`All walls are painted and you have ${Math.abs(total)} l paint left!`);   
            } else {
                console.log(`All walls are painted! Great job, Pesho!`);
            }
            break;
        }
    }
}

renovation([3, 5, 10, 2, 3, 4, 'Tired!']);  // Should return:
// 45 quadratic m left.

renovation([2, 3, 25, 6, 7, 8]);  // Should return:
// All walls are painted and you have 3 l paint left!