function matchTickets(input) {
    let budget = Number(input.shift());
    let category = input.shift();  // "VIP": 499.99 or "Normal: 249.99"
    let countPeople = Number(input.shift());

    let ticket = {"VIP": 499.99, "Normal": 249.99}[category];

    let transport = 0
    if (countPeople >= 1 && countPeople <= 4) {
        transport = budget * 0.75;
    } else if (countPeople >= 5 && countPeople <= 9) {
        transport = budget * 0.60;
    } else if (countPeople >= 10 && countPeople <= 24) {
        transport = budget * 0.50;
    } else if (countPeople >= 25 && countPeople <= 49) {
        transport = budget * 0.40;
    } else if (countPeople >= 50){
        transport = budget * 0.25;
    }

    let price = (ticket * countPeople) + transport;

    if (budget >= price) {
        console.log(`Yes! You have ${(budget - price).toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${(price - budget).toFixed(2)} leva.`);
    }
}

matchTickets(['1000', 'Normal', '1']);  // Expected Output:
// Yes! You have 0.01 leva left.


matchTickets(['30000', 'VIP', '49']);  // Expected Output:
// Not enough money! You need 6499.51 leva.


