function oscarsCeremony(params) {
    let rent = Number(params.shift());
    let totems = rent * 0.7;
    let catering = totems * 0.85;
    let sound = catering / 2;

    let total = rent + totems + catering + sound;
    
    console.log(total.toFixed(2));
}


oscarsCeremony(['3500']);  // Expected Output: 9073.75
oscarsCeremony(['5555']);  // Expected Output: 14401.34