function spice (...args) {
    let workingDays = 0;
    let yield = args.shift()
    let extracted = 0;
    while(yield >= 100) {
        workingDays += 1;
        extracted += yield - 26;
        yield -= 10;
    }
    extracted -= 26;
    extracted < 0 ? extracted = 0 : 'pass';

    console.log(workingDays);
    console.log(extracted);
}

spice(111);
spice(450);