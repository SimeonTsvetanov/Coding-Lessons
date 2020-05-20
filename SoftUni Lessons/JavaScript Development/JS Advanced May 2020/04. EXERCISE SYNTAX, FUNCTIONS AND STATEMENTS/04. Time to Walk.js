function timeToWalk(arg1, arg2, arg3) {
    let stepsNumber = Number(arg1);
    let stepsMetersHr = Number(arg2);
    let studentSpeed = Number(arg3);
  
    let distanceMeters = stepsNumber * stepsMetersHr;
    let speedMetersSec = studentSpeed / 3.6;
    let time = distanceMeters / speedMetersSec;
    let rest = Math.floor(distanceMeters / 500);
  
    let timeMin = Math.floor(time / 60);
    let timeSec = Math.round(time - (timeMin * 60));
    let timeHr = Math.floor(time / 3600);
  
    console.log((timeHr < 10 ? "0" : "") 
    + timeHr + ":" 
    + (timeMin + rest < 10 ? "0" : "") 
    + (timeMin + rest) + ":" 
    + (timeSec < 10 ? "0" : "") 
    + timeSec);
}

timeToWalk(4000, 0.60, 5);  // Should return: 00:32:48

timeToWalk(2564, 0.70, 5.5);  // Should return: 00:22:35
