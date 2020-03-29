function graduationPtTwo(params) {
    let name = params.shift();
    
    let scores = 0;
    let failed = false
    let grade = 1;
    let graduation = 12;
  
    while (grade <= graduation) {
        let score = Number(params.shift());
        
        if (score < 4) {
            if (failed) {
                console.log(`${name} has been excluded at ${grade} grade`);
                break;
            }
            failed = true;
            continue;
        }
        scores += score;
        grade += 1;
    }

    if (!failed) {
        let averageScore = (scores / 12).toFixed(2);
        console.log(`${name} graduated. Average grade: ${averageScore}`);
    }
}

graduationPtTwo(['Gosho', 5, 5.5, 6, 5.43, 5.5, 6, 5.55, 5, 6, 6, 5.43, 5]);
// Expected Output:
// Gosho graduated. Average grade: 5.53