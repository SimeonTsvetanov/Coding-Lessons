function travelling(input) {
    // Mask
    while ('command End') {
        let destination = input.shift();
        if (destination == "End") {break;}
        
        let price = Number(input.shift());

        while(price > 0) {
            price -= Number(input.shift());
        }

        console.log(`Going to ${destination}!`)
    }
}

travelling(['Greece', 1000, 200, 200, 300, 100, 150, 240, 'Spain', 1200, 300, 500, 193, 423, 'End']);  
// Should return:
// Going to Greece!
// Going to Spain!

travelling(['France', 2000, 300, 300, 200, 400, 190, 258, 360, 'Portugal', 1450, 400, 400, 200, 300, 300, 'Egypt', 1900, 1000, 280, 300, 500, 'End']);  
// Should return:
// Going to France!
// Going to Portugal!
// Going to Egypt!
