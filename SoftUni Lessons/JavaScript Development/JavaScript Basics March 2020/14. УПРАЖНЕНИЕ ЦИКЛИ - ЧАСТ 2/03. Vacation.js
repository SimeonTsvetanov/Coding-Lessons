function vacantion(data) {
    let needed = Number(data.shift());
    let money = Number(data.shift());

    let days = 0;
    let spendDays = 0;

    while ('Jessy has enugh money or spends money for 5 days in a row.') {
        let spendOrSave = data.shift();
        let amount = Number(data.shift());

        if (spendOrSave === 'save') {
            money += amount;
            spendDays = 0;
            days += 1;
            if (money >= needed) {
                console.log(`You saved the money for ${days} days.`);
                break;
            }
        } else if (spendOrSave === 'spend') {
            money -= amount;
            if (money < 0) {money = 0;}
            spendDays += 1
            days += 1
            if (spendDays == 5) {
                console.log(`You can't save the money.`);
                console.log(`${days}`)
                break;
            }
        }
    }
}

vacantion(['2000', '1000', 'spend', '1200', 'save', '2000']);
// Expected Output:
// You saved the money for 2 days.

vacantion(['110', '60', 'spend', '10', 'spend', '10', 'spend', '10', 'spend', '10', 'spend', '10']);
// Expected Output:
// You can't save the money.
// 5
