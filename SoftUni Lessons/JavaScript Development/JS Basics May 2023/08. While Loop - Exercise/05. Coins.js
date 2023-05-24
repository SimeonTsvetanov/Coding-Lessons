function coins(data) {
    // it will most likely break the time limit. BUT it's much simpler yet ugly solution
    
    let amount = Number(data.shift()) * 100;

    let coins = 0;

    while(amount > 0) {
        [200, 100, 50, 20, 10, 5, 2, 1].forEach(i => {
            while(i <= amount) {amount -= i; coins += 1;}
        });
    }

    console.log(coins);
}

coins(["1.23"])
// 4

console.log('********************************');

coins(["2"])
// 1
