// Not included in final score

function cleverLily(params) {
    let lilyAge = Number(params.shift());
    let washingMachinePrice = Number(params.shift());
    let oneToyPrice = Number(params.shift());

    let birthdayMoney = 0;
    let toys = 0;

    for (let year = 1; year <= lilyAge; year++) {
        if (year % 2 != 0) {toys += 1;}
        else {birthdayMoney += (year * 5) - 1;}
    }

    let savedMoney = birthdayMoney + (toys * oneToyPrice);
    
    if (savedMoney >= washingMachinePrice) {
        console.log(`Yes! ${Math.abs(savedMoney - washingMachinePrice).toFixed(2)}`);
    } else {
        console.log(`No! ${Math.abs(washingMachinePrice - savedMoney).toFixed(2)}`);
    }
}


cleverLily([10, 170.00, 6])
