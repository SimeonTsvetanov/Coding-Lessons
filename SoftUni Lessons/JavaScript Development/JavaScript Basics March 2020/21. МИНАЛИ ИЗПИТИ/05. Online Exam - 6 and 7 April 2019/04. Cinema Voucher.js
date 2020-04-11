function cinemaVouchers(input) {
    // Mask
    let vaucher = Number(input.shift());

    let tickets = 0;
    let products = 0;

    while ('End, or No more VCH') {
        let name = input.shift();
        if (name == "End") {
            break;
        }

        if (name.length > 8) {
            // It's a Movie (SIT DOWN AND GET DUM)
            let price = name.charCodeAt(0) + name.charCodeAt(1);
            if (vaucher - price < 0) {break;}
            vaucher -= price
            tickets += 1
        } else {
            // IT's a Product: (OVERPRICED FAT MAKER)
            let price = name.charCodeAt(0);
            if (vaucher - price < 0) {break;}
            vaucher -= price
            products += 1
        }
    }
    
    console.log(tickets);
    console.log(products);
}

cinemaVouchers([300, 'Captain Marvel', 'popcorn', 'Pepsi']);  // Should return:
// 1
// 1

cinemaVouchers([1500, 'Avengers: Endgame', 'Bohemian Rhapsody', 'Deadpool 2', 'End']);  // Should return:
// 3
// 0