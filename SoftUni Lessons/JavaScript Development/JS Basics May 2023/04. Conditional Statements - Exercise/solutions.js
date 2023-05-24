function sumSeconds(params) {
    let time = params.map(Number).reduce((a, b) => a + b, 0);
    console.log(Math.floor(time / 60) + ':' + ('0' + Math.floor(time % 60)).slice(-2));
}

// sumSeconds(['35', '45', '44']);  // 2:04
// sumSeconds(["50", "50", "49"]);  //2:29

function bonusScore(params) {
    let num = Number(params[0]);
    let score = 0

    if (num <= 100) { score += 5; } 
    else if (num > 100 && num <= 1000) { score += (num * 0.2); }
    else if (num > 1000) { score += (num * 0.1); }

    if (num % 2 === 0) { score += 1; }
    else if (num % 5 === 0) { score += 2; }

    console.log(score);
    console.log(score + num);
}

// bonusScore(['20']);  // 6
// bonusScore(['175']);  // 37
// bonusScore(['2703']);  // 270.3

function timePlus15Minutes(params) {
    let hours = Number(params.shift());
    let minutes = Number(params.shift()) + 15;

    if (minutes > 59) {
        hours += 1;
        minutes -= 60;
    } 
    
    if (hours > 23) {
        hours -= 24;
    }
    
    if (minutes < 10) {
        console.log(`${hours}:0${minutes}`);
    } else {
        console.log(`${hours}:${minutes}`);
    }
}

// timePlus15Minutes((["1", "46"]));  // 2:01
// timePlus15Minutes((["0", "01"]));  // 0:16
// timePlus15Minutes((["23", "59"]));  // 0:14

function toyShop(params) {
    let excursionPrice = Number(params.shift());
    let toysCount = params.map(Number).reduce((a,b) => a + b, 0);
    let puzzles = Number(params.shift()) * 2.6;
    let dolls = Number(params.shift()) * 3;
    let bears = Number(params.shift()) * 4.1;
    let minions = Number(params.shift()) * 8.2;
    let trucks = Number(params.shift()) * 2;
    let total = puzzles + dolls + bears + minions + trucks;

    if (toysCount >= 50) {total = total *= 0.75};
    total = total * 0.9;

    if (total >= excursionPrice) {
        console.log(`Yes! ${(total - excursionPrice).toFixed(2)} lv left.`);
    } else {
        console.log(`Not enough money! ${(excursionPrice - total).toFixed(2)} lv needed.`);
    }
}

// toyShop((["40.8",
// "20",
// "25",
// "30",
// "50",
// "10"])
// );  // Yes! 418.20 lv left.

// toyShop(["320",
// "8",
// "2",
// "5",
// "5",
// "1"]);  // Not enough money! 238.73 lv needed.

function godzillaVsKong(params) {
    let budget = Number(params.shift());
    let statists = Number(params.shift());
    let priceCloth = Number(params.shift());
    let decorPrice = budget * 0.1;
    let totalCloth = statists * priceCloth;
    if (statists > 150) {totalCloth = totalCloth * 0.9}
    let total = decorPrice + totalCloth;
    
    if (total > budget) {
        console.log(`Not enough money!`);
        console.log(`Wingard needs ${(total - budget).toFixed(2)} leva more.`);
    } else {
        console.log(`Action!`);
        console.log(`Wingard starts filming with ${(budget - total).toFixed(2)} leva left.`);
    }
}

// godzillaVsKong([
//     "20000",
//     "120",
//     "55.5"
// ]);
// // Action!
// // Wingard starts filming with 11340.00 leva left.

// godzillaVsKong([
//     "15437.62",
//     "186",
//     "57.99"
// ]);
// // Action!
// // Wingard starts filming with 4186.33 leva left.

// godzillaVsKong([
//     "9587.88",
//     "222",
//     "55.68"
// ]);
// // Not enough money!
// // Wingard needs 2495.77 leva more.

function worldSwimmingRecord(params) {
    let currentRecord = Number(params.shift());
    let distance = Number(params.shift());
    let timeInSeconds = Number(params.shift());
    
    let time = (distance * timeInSeconds) + (Math.floor(distance / 15)) * 12.5;

    if (time > currentRecord) {
        console.log(`No, he failed! He was ${(time - currentRecord).toFixed(2)} seconds slower.`);
    } else {
        console.log(`Yes, he succeeded! The new world record is ${time.toFixed(2)} seconds.`);
    }
}

// worldSwimmingRecord(["10464",
// "1500",
// "20"]);
// // No, he failed! He was 20786.00 seconds slower.

// worldSwimmingRecord(["55555.67",
// "3017",
// "5.03"]);
// // Yes, he succeeded! The new world record is 17688.01 seconds.

function shopping(params) {
    let budget = Number(params.shift());
    let videoCount = Number(params.shift());
    let video = videoCount * 250;
    let processorCount = Number(params.shift());
    let processors = processorCount * (video * 0.35);
    let ram = Number(params.shift()) * (video * 0.1);
    let total = video + processors + ram;
    (videoCount > processorCount) ? total *= 0.85 : 'pass';
    let happy = `You have ${(budget - total).toFixed(2)} leva left!`;
    let sad = `Not enough money! You need ${(total - budget).toFixed(2)} leva more!`;
    (budget >= total) ? console.log(happy) : console.log(sad);
}

// shopping(["900",
// "2",
// "1",
// "3"]);
// // You have 198.75 leva left!

// shopping((["920.45",
// "3",
// "1",
// "1"])
// );
// // Not enough money! You need 3.92 leva more!

function lunchBreak(params) {
    let series = params.shift();
    let seriesDuration = Number(params.shift());
    let breakDuration = Number(params.shift());

    let lunchTime = breakDuration / 8;
    let breakTime = breakDuration * 0.25;

    let timeNeeded = breakDuration - lunchTime - breakTime;
    
    let happy = `You have enough time to watch ${series} and left with ${Math.ceil(timeNeeded - seriesDuration)} minutes free time.`;
    let sad = `You don't have enough time to watch ${series}, you need ${Math.ceil(seriesDuration - timeNeeded)} more minutes.`;

    (timeNeeded >= seriesDuration) ? console.log(happy) : console.log(sad);
}

lunchBreak(["Game of Thrones",
"60",
"96"])
// You have enough time to watch Game of Thrones and left with 0 minutes free time.

lunchBreak(["Teen Wolf",
"48",
"60"])
// You don't have enough time to watch Teen Wolf, you need 11 more minutes.
