function oddEvenSum(...params) {
    let times = Number(params.shift());

    let evenSum = 0;
    let oddSum = 0;

    for (let eachTime = 1; eachTime <= times; eachTime++) {
        if (eachTime % 2 != 0) {oddSum += Number(params.shift());}
        else {evenSum += Number(params.shift());}
    }

    if (evenSum == oddSum) {console.log(`Yes\nSum = ${evenSum}`);}
    else {console.log(`No\nDiff = ${Math.abs(evenSum - oddSum)}`);}
}

oddEvenSum(4, 10, 50, 60, 20);
