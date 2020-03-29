function graduation(params) {
    let name = params.shift();
    
    let scores = 0;

    let grade = 1;
    let graduation = 12;
    while (grade <= graduation) {
        let score = Number(params.shift());
        
        if (score < 4) {
            continue;
        }

        scores += score;
        grade += 1;
    }

    averageScore = (scores / 12).toFixed(2)
    console.log(`${name} graduated. Average grade: ${averageScore}`);
}

graduation(['Pesho', 4, 5.5, 6, 5.43, 4.5, 6, 5.55, 5, 6, 6, 5.43, 5]); // Expected Output:
// Pesho graduated. Average grade: 5.37
