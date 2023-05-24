function salaryCheck(params) {
    let count = Number(params.shift());
    let salary = Number(params.shift());

    let penalties = {
        "Facebook": 150,
        "Instagram": 100,
        "Reddit": 50,
    }

    for (let i = 0; i < count; i++) {
        let website = params.shift();
        if (website in penalties) {
            salary -= penalties[website];
            if (salary <= 0) {
                console.log(`You have lost your salary.`);
                break;
            }
        }
    }

    if (salary > 0) {
        console.log(Math.round(salary));
    }
}

salaryCheck(["10",
"750",
"Facebook",
"Dev.bg",
"Instagram",
"Facebook",
"Reddit",
"Facebook",
"Facebook"]);
// You have lost your salary.

salaryCheck(["3",
"500",
"Github.com",
"Stackoverflow.com",
"softuni.bg"]);
// 500

salaryCheck(["3",
"500",
"Facebook",
"Stackoverflow.com",
"softuni.bg"]);
// 350