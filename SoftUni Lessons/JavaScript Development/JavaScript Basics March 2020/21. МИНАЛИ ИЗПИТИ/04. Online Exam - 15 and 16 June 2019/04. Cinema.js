function cinema(input) {
    // Mask
    let seats = Number(input.shift());
    let total = 0;
   
    while('you want to...') {
        let command = input.shift();
        if (command == 'Movie time!') {
            console.log(`There are ${seats} seats left in the cinema.`);
            break;
        }

        let group = Number(command);
        
        if (seats - group < 0) {
            console.log(`The cinema is full.`);
            break;
        }
        seats -= group;

        price = group * 5;
        if (group % 3 == 0) {price -= 5;}

        total += price;
    }

    console.log(`Cinema income - ${total} lv.`)
}

cinema([60, 10, 6, 3, 20, 15, 'Movie time!']);  // Should return:
// There are 6 seats left in the cinema.
// Cinema income - 255 lv.

cinema([50, 15, 10, 10, 15, 5]);  // Should return:
// The cinema is full.
// Cinema income - 240 lv.
