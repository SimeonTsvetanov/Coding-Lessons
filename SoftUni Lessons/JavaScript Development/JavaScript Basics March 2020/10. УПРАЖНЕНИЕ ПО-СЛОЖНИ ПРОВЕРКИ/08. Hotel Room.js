function HotelRoom(...input) {
    let month = input.shift();
    let nights = Number(input.shift());

    let studio = 0;
    let apartament = 0;

    if (month === "May" || month === "October") {
        studio = 50;
        apartament = 65;
        if (nights > 7 && nights <= 14) {
            studio *= 0.95;
        } else if (nights > 14) {
            studio *= 0.7;
        }
    } else if (month === "June" || month === "September") {
        studio = 75.20;
        apartament = 68.70;
        if (nights > 14) {
            studio *= 0.8;
        }
    } else if (month === "July" || month === "August") {
        studio = 76;
        apartament = 77;
    }
    if (nights > 14) {
        apartament *= 0.9;
    }

    console.log(`Apartment: ${(apartament * nights).toFixed(2)} lv.`)
    console.log(`Studio: ${(studio * nights).toFixed(2)} lv.`)
}

HotelRoom(['May', '15']);  // Expected Output:
// Apartment: 877.50 lv.
// Studio: 525.00 lv.

HotelRoom(['June', '14']);  // Expected Output:
// Apartment: 961.80 lv.
// Studio: 1052.80 lv.

HotelRoom(['August', '20']);  // Expected Output:
// Apartment: 1386.00 lv.
// Studio: 1520.00 lv.
