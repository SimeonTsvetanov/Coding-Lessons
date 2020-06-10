function attachEventsListeners() {
    let days = document.querySelector('#days');       // Get the days input value
    let hours = document.querySelector('#hours');     // Get the hours input value
    let minutes = document.querySelector('#minutes'); // Get the seconds input value
    let seconds = document.querySelector('#seconds'); // Get the minutes input value

    // From Days
    document.querySelector('#daysBtn').addEventListener('click', function (e) {
        hours.value = days.value * 24; 
        minutes.value = days.value * 1440;
        seconds.value = days.value * 86400;
    })

    // From Hours
    document.querySelector('#hoursBtn').addEventListener('click', function (e) {
        days.value = hours.value / 24;
        minutes.value = hours.value * 60;
        seconds.value = hours.value * 3600;
    })

    // From Minutes
    document.querySelector('#minutesBtn').addEventListener('click', function (e) {
        days.value = minutes.value / 1440;
        hours.value = minutes.value / 60
        seconds.value = minutes.value * 60;
    })

    // From Seconds
    document.querySelector('#secondsBtn').addEventListener('click', function (e) {
        days.value = seconds.value / (3600*24);
        hours.value = seconds.value / 60 / 60;
        minutes.value = seconds.value / 60;
    })
}
