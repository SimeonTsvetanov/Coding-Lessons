function mask (params) {
    // MASK -> Stupid TASK missing argument in description can cost you a lot of time....
    // When you have battle after the match is over, and we delete the fighter we need to stop the LOOP
    // Or else it will keep on searching for new matching skills on a missing person and judge won't like it!
    let pool = {}

    for (const param of params) {
        if (param.includes(' -> ')) {
            let gladiator = param.split(' -> ')[0];
            let technique = param.split(' -> ')[1];
            let skill = Number(param.split(' -> ')[2]);

            if (!(gladiator in pool)) {
                pool[gladiator] = {}
                pool[gladiator][technique] = skill;
            } else if (!(technique in pool[gladiator])) {
                pool[gladiator][technique] = skill;
            } else if (technique in pool[gladiator]) {
                pool[gladiator][technique] = Math.max(pool[gladiator][technique], skill);
            }

        } else if (param.includes(' vs ')) {
            let [gladiatorOne, gladiatorTwo] = param.split(' vs ');
            if ((gladiatorOne in pool) && (gladiatorTwo in pool)) {
                let battleOver = false;
                for (let [techOne, pointsOne] of Object.entries(pool[gladiatorOne])) {
                    if (battleOver) { break; }
                    for (let [techTwo, pointsTwo] of Object.entries(pool[gladiatorTwo])) {
                        if (battleOver) { break; }
                        if (techOne === techTwo) {
                            let totalSkillOne = Object.values(pool[gladiatorOne]).reduce((a, b) => a + b, 0);
                            let totalSkillTwo = Object.values(pool[gladiatorTwo]).reduce((a, b) => a + b, 0);
                            if (totalSkillOne > totalSkillTwo) {
                                delete pool[gladiatorTwo];
                                battleOver = true;
                            } else if (totalSkillTwo > totalSkillOne){
                                delete pool[gladiatorOne];
                                battleOver = true;
                            }
                        }
                    }
                }
            }
        } else if (param === "Ave Cesar"){
            break;
        }
    }

    for (let [gladiator, techniques] of Object.entries(pool)
        .sort((a, b) => {
            let totalOne = Object.values(a[1]).reduce((a, b) => a + b, 0);
            let totalTwo = Object.values(b[1]).reduce((a, b) => a + b, 0);
            if (totalOne !== totalTwo) {
                return totalTwo - totalOne;
            }
            return a[0].localeCompare(b[0])
    })) {
        let totalSkill = Object.values(techniques).reduce((a, b) => a + b, 0);
        console.log(`${gladiator}: ${totalSkill} skill`);
        for (let [technique, skill] of Object.entries(techniques)
            .sort((a, b) => {
                if (a[1] !== b[1]) {
                    return b[1] - a[1];
                }
                return a[0].localeCompare(b[0]);
            })) {
            console.log(`- ${technique} <!> ${skill}`);
        }
    }
}

mask([
'Peter -> BattleCry -> 400',
'Alex -> PowerPunch -> 300',
'Stefan -> Duck -> 200',
'Stefan -> Tiger -> 250',
'Ave Cesar'
]);
// Stefan: 450 skill
// - Tiger <!> 250
// - Duck <!> 200
// Peter: 400 skill
// - BattleCry <!> 400
// Alex: 300 skill
// - PowerPunch <!> 300

console.log('-------------------------------------');

mask([
'Peter -> Duck -> 400',
'Julius -> Shield -> 150',
'Gladius -> Heal -> 200',
'Gladius -> Support -> 250',
'Gladius -> Shield -> 250',
'Peter vs Gladius',
'Gladius vs Julius',
'Gladius vs Maximilian',
'Ave Cesar'
]);
// Gladius: 700 skill
// - Shield <!> 250
// - Support <!> 250
// - Heal <!> 200
// Peter: 400 skill
// - Duck <!> 400
