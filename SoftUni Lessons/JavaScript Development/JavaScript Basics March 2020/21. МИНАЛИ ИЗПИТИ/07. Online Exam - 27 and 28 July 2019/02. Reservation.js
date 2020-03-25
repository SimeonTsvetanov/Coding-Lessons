function reservation(params) {
    let dayReservation = Number(params.shift());
    let mothReservation = Number(params.shift());
    let dayAccommodation = Number(params.shift());
    let monthAccommodation = Number(params.shift());
    let dayDeparture = Number(params.shift());
    let monthDeparture = Number(params.shift());

    let nightPrice = 30;

    if (dayAccommodation - dayReservation >= 10) {
        nightPrice = 25;
    }

    if (mothReservation < monthAccommodation) {
        nightPrice = 25 * 0.8;
    }

    let price = (dayDeparture - dayAccommodation) * nightPrice;
    
    console.log(`Your stay from ${dayAccommodation}/${monthAccommodation} to ${dayDeparture}/${monthAccommodation} will cost ${price.toFixed(2)}`);
}


reservation([21, 7, 28, 8, 30, 8]);  // Expected Output:
// Your stay from 28/8 to 30/8 will cost 40.00

reservation([10, 5, 15, 5, 18, 5]);  // Expected Output:
// Your stay from 15/5 to 18/5 will cost 90.00

reservation([20, 10, 5, 11, 10, 11]);  // Expected Output:
// Your stay from 5/11 to 10/11 will cost 100.00