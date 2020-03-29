function coins(data) {
    let amount = Number(data.shift()) * 100;

    let coins = 0;

    while(200 <= amount) {amount -= 200; coins += 1;}
    while(100 <= amount) {amount -= 100; coins += 1;}
    while(50 <= amount) {amount -= 50; coins += 1;}
    while(20 <= amount) {amount -= 20; coins += 1;}
    while(10 <= amount) {amount -= 10; coins += 1;}
    while(5 <= amount) {amount -= 5; coins += 1;}
    while(2 <= amount) {amount -= 2; coins += 1;}
    while(1 <= amount) {amount -= 1; coins += 1;}

    console.log(coins);
}


coins([1.23]);  // Expected Output: 4
coins([2]);  // Expected Output: 1
coins([0.56]);  // Expected Output: 3
coins([2.73]);  // Expected Output: 5