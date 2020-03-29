function walking(data) {
    let steps = 0;
    
    while ("Steps >= 10 000 or Gaby want's to go home early") {
        let count = data.shift();
        if (count === 'Going home') {
            steps += Number(data.shift());
            if (steps >= 10000) {
                console.log(`Goal reached! Good job!`)
                break;
            } else {
                console.log(`${10000 - steps} more steps to reach goal.`);
                break;
            }
        }
        steps += Number(count);
    
        if (steps >= 10000) {
            console.log(`Goal reached! Good job!`)
            break;
        } 
    }
}

walking([1000, 1500, 2000, 6500]);
// Expected Output:
// Goal reached! Good job!

walking([1500, 300, 2500, 3000, 'Going home', 200]);
// Expected Output:
// 2500 more steps to reach goal.