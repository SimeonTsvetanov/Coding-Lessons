function stopwatch() {
    let seconds = 0;  // Initial seconds Value 
    let minutes = 0;  // Initial minutes Value
    let intervalID;   // Declare the Interval

    // Get the buttons and the Time Stamp:
    const time = document.querySelector('#time');
    const startBtn = document.querySelector('#startBtn');
    const stopBtn = document.querySelector('#stopBtn');
    
    // When the start button is pressed:
    function startBtnHandler (e) {
        // First WE need to RESTART the time:
        time.innerText = "00:00";
        seconds = 0;
        minutes = 0;
        // Now Swap the buttons DISABLED property
        startBtn.setAttribute('disabled', 'true');
        stopBtn.removeAttribute('disabled');
        // Now start the time Interval:
        intervalID = setInterval(function () {
            seconds += 1;  // Increment the time with 1 second
            // Check if we need to increment the minutes:
            if (seconds === 60) {
                seconds = 0;
                minutes += 1;

            }
            // And set the output to be with leading ZERO:
            let minutesText;
            let secondsText;
            minutes < 10 ? minutesText = `0${minutes}` : minutesText = minutes;
            seconds < 10 ? secondsText = `0${seconds}` : secondsText = seconds;
            // Set the time on the screen:
            time.innerText = `${minutesText}:${secondsText}`;
        },
        1000 // This is the time Delta or 1 second!
        );
    }

    // when the stop button is pressed:
    function stopBtnHandler (e) {
        stopBtn.setAttribute('disabled', 'true');  // Disable the Stop Button
        startBtn.removeAttribute('disabled');      // Enable the Start Button
        clearInterval(intervalID);                 // Stop the Interval Delta
    }

    startBtn.addEventListener('click', startBtnHandler);  // Add the Listened for start
    stopBtn.addEventListener('click', stopBtnHandler);    // Add the Listened for stop
}