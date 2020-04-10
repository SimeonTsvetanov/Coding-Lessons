function oscars(input) {
    // Mask
    let name = input.shift();
    let points = Number(input.shift());
    let judges = Number(input.shift());

    for (let judge = 1; judge <= judges; judge += 1) {
        let judgeName = input.shift();
        points += judgeName.length * Number(input.shift()) / 2;

        if (points > 1250.5) {
            console.log(`Congratulations, ${name} got a nominee for leading role with ${points.toFixed(1)}!`);
            break;
        }
    }

    if (points <= 1250.5) {
        console.log(`Sorry, ${name} you need ${(1250.5 - points).toFixed(1)} more!`);
    }
}

oscars(['Zahari Baharov', 205, 4, 'Johnny Depp', 45, 'Will Smith', 29, 'Jet Lee', 10, 'Matthew Mcconaughey', 39]);  
// Should return:
// Sorry, Zahari Baharov you need 247.5 more!

oscars(['Sandra Bullock', 340, 5, 'Robert De Niro', 50, 'Julia Roberts', 40.5, 'Daniel Day-Lewis', 39.4, 'Nicolas Cage', 29.9, 'Stoyanka Mutafova', 33]);  
// Should return:
// Congratulations, Sandra Bullock got a nominee for leading role with 1268.5!