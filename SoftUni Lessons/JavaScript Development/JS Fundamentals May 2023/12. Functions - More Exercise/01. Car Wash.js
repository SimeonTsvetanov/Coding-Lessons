function carWash(commands) {
    // MasK
    let services = {
        'soap': (current) => {return 10},
        'water': (current) => {return current * 0.2},
        'vacuum cleaner': (current) => {return current * 0.25},
        'mud': (current) => {return -(current * 0.10)}
    };

    let cleaned = 0;

    commands.forEach(command => {
        cleaned += services[command](cleaned);
    });

    return `The car is ${cleaned.toFixed(2)}% clean.`;
}

console.log(carWash(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water']));
console.log(carWash(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]));

