function solution(params) {
    // MasK
    while (true) {
        let destination = params.shift();
        if (destination === 'End') {
            break;
        }
        let budget = Number(params.shift());
        let savings = 0;
        while (savings < budget) {
            savings += Number(params.shift());
        }
        console.log(`Going to ${destination}!`);
    }
}

solution(["Greece",
"1000",
"200",
"200",
"300",
"100",
"150",
"240",
"Spain",
"1200",
"300",
"500",
"193",
"423",
"End"])

// Going to Greece!
// Going to Spain!

console.log('********************************');

solution(["France",
"2000",
"300",
"300",
"200",
"400",
"190",
"258",
"360",
"Portugal",
"1450",
"400",
"400",
"200",
"300",
"300",
"Egypt",
"1900",
"1000",
"280",
"300",
"500",
"End"])

// Going to France!
// Going to Portugal!
// Going to Egypt!