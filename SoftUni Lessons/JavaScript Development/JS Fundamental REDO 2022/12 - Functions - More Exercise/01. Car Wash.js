function carWash(commands) {
    let value = 0;
    
    let cleaning = {
        'soap': (value) => { return value += 10; },
        'water': (value) => { return value += value * 0.2; },
        'vacuum cleaner': (value) => { return value += value * 0.25; },
        'mud': (value) => { return value -= value * 0.1; }
    }

    commands.forEach(command => {
        value = cleaning[command](value);
    });

    console.log(`The car is ${value.toFixed(2)}% clean.`);
}

carWash(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water'])
// The car is 39.00% clean.

carWash(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]);
// The car is 13.12% clean.