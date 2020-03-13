// This is probably, most likly, for sure the ugliest TASK SoftUni has...!

function onTimeForTheExam(input) {
    let hourExam = Number(input.shift());
    let minuteExam = Number(input.shift());
    let hourArrival = Number(input.shift());
    let minuteArrival = Number(input.shift());

    let differenceMinutes = ((hourExam * 60) + minuteExam) - ((hourArrival * 60) + minuteArrival);

    let hh = Math.abs(~~(differenceMinutes / 60));
    let mm = Math.abs(differenceMinutes % 60);
    if (mm == 0) {mm = `00`}
    let time = 0;
    if (hh == 0) {
        time = `${mm} minutes`;
    } else {
        if (Number(mm) <= 9 && Number(mm) != 0) {mm = `0${mm}`}
        time = `${hh}:${mm} hours`;
    }

    let beforeOrAfter = '';

    if (differenceMinutes >= 0 && differenceMinutes <= 30) {
        console.log('On time');
        beforeOrAfter = 'before';
    } else if (differenceMinutes > 30) {
        console.log('Early');
        beforeOrAfter = 'before';
    } else if (differenceMinutes < 0) {
        console.log('Late');
        beforeOrAfter = 'after';
    }

    if (Math.abs(differenceMinutes) > 0) {
        // Only if difference is bigger then one minute it will print more:
        console.log(`${time} ${beforeOrAfter} the start`);
    }
}

onTimeForTheExam(['9', '30', '9', '50']);  //Expected Output:
// Late
// 20 minutes after the start

onTimeForTheExam(['9', '00', '10', '30']);  //Expected Output:
// Late
// 1:30 hours after the start

onTimeForTheExam(['10', '00', '10', '00']);  //Expected Output:
// On time

onTimeForTheExam(['9', '00', '8', '30']);  //Expected Output:
// On time
// 30 minutes before the start

onTimeForTheExam(['14', '00', '13', '55']);  //Expected Output:
// On time
// 5 minutes before the start

onTimeForTheExam(['11', '30', '10', '55']);  //Expected Output:
// Early
// 35 minutes before the start

onTimeForTheExam(['16', '00', '15', '00']);  //Expected Output:
// Early
// 1:00 hours before the start

onTimeForTheExam(['11', '30', '8', '12']);  //Expected Output:
// Early
// 3:18 hours before the start

onTimeForTheExam(['11', '30', '12', '29']);  //Expected Output:
// Late
// 59 minutes after the start
