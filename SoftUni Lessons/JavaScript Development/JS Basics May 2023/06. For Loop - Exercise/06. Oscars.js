function oscars(params) {
    let actor = params.shift();
    let points = Number(params.shift());
    let critics = Number(params.shift());
    
    let oscarPoints = 1250.5;

    for (let i = 0; i < critics; i++) {
        let critic = params.shift();
        let criticPoints = Number(params.shift());

        points += (critic.length * criticPoints) / 2;
        if (points >= oscarPoints) {
            break;
        }
    }

    let happy = `Congratulations, ${actor} got a nominee for leading role with ${points.toFixed(1)}!`;
    let sad = `Sorry, ${actor} you need ${(oscarPoints - points).toFixed(1)} more!`;

    (points >= oscarPoints) ? console.log(happy) : console.log(sad);
}

oscars(["Zahari Baharov",
"205",
"4",
"Johnny Depp",
"45",
"Will Smith",
"29",
"Jet Lee",
"10",
"Matthew Mcconaughey",
"39"]);
// Sorry, Zahari Baharov you need 247.5 more!

oscars(["Sandra Bullock",
"340",
"5",
"Robert De Niro",
"50",
"Julia Roberts",
"40.5",
"Daniel Day-Lewis",
"39.4",
"Nicolas Cage",
"29.9",
"Stoyanka Mutafova",
"33"]);
// Congratulations, Sandra Bullock got a nominee for leading role with 1268.5!
