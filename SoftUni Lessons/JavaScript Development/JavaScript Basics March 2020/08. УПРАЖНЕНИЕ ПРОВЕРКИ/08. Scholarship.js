// Not included in final score
// Short link: http://bit.ly/2WpVYWH
function scholarship(...input) {
    let income = Number(input.shift());
    let score = Number(input.shift());
    let minimumSalary = Number(input.shift());

    let socialScholarship = 0;
    let excellenceScholarship = 0;

    if ((income < minimumSalary) && (score > 4.5)) {
        socialScholarship = minimumSalary * 0.35;
    } 
    if (score >= 5.5) {
        excellenceScholarship = score * 25;
    }

    if (socialScholarship === 0 && excellenceScholarship === 0) {
        console.log("You cannot get a scholarship!");
    } else if (socialScholarship > excellenceScholarship) {
        console.log(`You get a Social scholarship ${Math.floor(socialScholarship)} BGN`);
    } else {
        console.log(`You get a scholarship for excellent results ${Math.floor(excellenceScholarship)} BGN`);
    }
}

scholarship(['480.00', '4.60', '450.00']);  // Expected Output: You cannot get a scholarship!
scholarship(['300.00', '5.65', '420.00']);  // Expected Output: You get a Social scholarship 147 BGN
