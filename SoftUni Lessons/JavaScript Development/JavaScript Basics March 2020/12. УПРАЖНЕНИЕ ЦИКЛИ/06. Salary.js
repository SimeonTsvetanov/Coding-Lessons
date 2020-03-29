function salary(params) {
    let tabs = Number(params.shift());
    let salary = Number(params.shift());
    
    let websites = {'Facebook': 150, 'Instagram': 100, 'Reddit': 50};
    let lost = false;

    for (let tab = 1; tab <= tabs; tab++) {
        website = params.shift();
        if (websites.hasOwnProperty(website)) {salary -= websites[website];}
        if (salary <= 0) {lost = true; break;}
    }
    if (lost) {console.log("You have lost your salary.");}
    else {console.log(parseInt(salary));}
}

salary(['10', '750', 'Facebook', 'Dev.bg', 'Instagram', 'Facebook', 'Reddit', 'Facebook', 'Facebook']);
// Expected Output:
// You have lost your salary.


salary([3, 500, 'Github.com', 'Stackoverflow.com', 'softuni.bg']);
// Expected Output:
// 500

salary([3, 500, 'Facebook', 'Stackoverflow.com', 'siftuni.bg']);
// Expected Output:
// 350
