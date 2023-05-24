function solution(params) {
    // MasK
    let needed = Number(params.shift());
    let saved = Number(params.shift());
    let days = 0;
    let spendDays = 0;

    while(params.length > 0) {
        days ++;
        let action = params.shift();
        let amount = Number(params.shift());

        if (action === 'spend') {  // Spending
            spendDays ++;
            if (spendDays === 5) {
                console.log(`You can't save the money.`);
                console.log(`${days}`);
                break
            }
            ((saved - amount) < 0) ? saved = 0 : saved -= amount;

        } else if (action === 'save') {  // Saving
            saved += amount;
            spendDays = 0;
            if (saved >= needed) {
                console.log(`You saved the money for ${days} days.`);
                break;
            }
        }
    }
}

solution(["2000",
"1000",
"spend",
"1200",
"save",
"2000"])

// You saved the money for 2 days.

console.log('********************************');

solution(["110",
"60",
"spend",
"10",
"spend",
"10",
"spend",
"10",
"spend",
"10",
"spend",
"10"])

// You can't save the money.
// 5
