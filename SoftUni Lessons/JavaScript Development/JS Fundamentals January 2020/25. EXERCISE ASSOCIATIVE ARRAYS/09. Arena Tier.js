function arenaTier (data) {
    // MasK - Now that's probably the biggest task in SoftUni!

    class Gladiator {
        constructor(name) {
            this.name = name;
            this.techniques = [];
        }

        addTechnique(newTechnique) {
            let presentTechnique = this.techniques.find(x => x.name === newTechnique.name)
            if (presentTechnique) {
                presentTechnique.power = Math.max(newTechnique.power, presentTechnique.power);
            } else {
                this.techniques.push(newTechnique);
            }
        }

        get totalSkill() {
            let sum = 0;
            this.techniques.forEach(tech => {
                sum += tech.power;
            });
            return sum;
        }
    }

    function fight(gladiatorOne, gladiatorTwo) {
        // Check if we have matching skills:
        let fightOver = false;
        for (let g1Tech of gladiatorOne.techniques) {
            if (fightOver) {break;}
            for (let g2Tech of gladiatorTwo.techniques) {
                if (g1Tech.name === g2Tech.name) {
                    // We have a fight:
                    if (g1Tech.power > g2Tech.power) {
                        gladiators.splice(gladiators.indexOf(gladiatorTwo), 1);
                        fightOver = true;
                        break;
                    } else if (g2Tech.power > g1Tech.power) {
                        gladiators.splice(gladiators.indexOf(gladiatorOne), 1);
                        fightOver = true;
                        break;
                    }
                }
            }
        }
    }

    let gladiators = [];

    for (let entry of data) {
        if (entry === 'Ave Cesar') { break; }

        else if (entry.includes(' -> ')) {
            // We need to add or update gladiator:
            let name = entry.split(' -> ')[0];
            let techniqueName = entry.split(' -> ')[1];
            let power = +entry.split(' -> ')[2];

            let technique = {'name': techniqueName, 'power': power};

            let gladiator = gladiators.find(x => x.name === name);
            if (!gladiator) {
                gladiator = new Gladiator(name);
                gladiator.addTechnique(technique);
                gladiators.push(gladiator)
            } else {
                gladiator.addTechnique(technique);
            }
        } else if (entry.includes('vs')) {
            //  We have a battle:
            let g1Name = entry.split(' vs ')[0];
            let g2Name = entry.split(' vs ')[1];
            let gladiatorOne = gladiators.find(x => {return x.name === g1Name});
            let gladiatorTwo = gladiators.find(x => {return x.name === g2Name});
            if (gladiatorOne && gladiatorTwo) {
                fight(gladiatorOne, gladiatorTwo);
            }
        }
    }

    gladiators.sort((a, b) => {
        if (a.totalSkill !== b.totalSkill) {
            return b.totalSkill - a.totalSkill;
        }
        return a.name.localeCompare(b.name);
    });

    gladiators.forEach(gladiator => {
        console.log(`${gladiator.name}: ${gladiator.totalSkill} skill`);
        gladiator.techniques.sort((a, b) => {
            if (a.power !== b.power) {
                return b.power - a.power;
            }
            return a.name.localeCompare(b.name)
        })
        gladiator.techniques.forEach(tech => {
            console.log(`- ${tech.name} <!> ${tech.power}`);
        });
    });
}

arenaTier([
        'Peter -> BattleCry -> 400',
        'Alex -> PowerPunch -> 300',
        'Stefan -> Duck -> 200',
        'Stefan -> Tiger -> 250',
        'Ave Cesar'
    ]
);

// Stefan: 450 skill
// - Tiger <!> 250
// - Duck <!> 200
// Peter: 400 skill
// - BattleCry <!> 400
// Alex: 300 skill
// - PowerPunch <!> 300

console.log();

arenaTier([
        'Peter -> Duck -> 400',
        'Julius -> Shield -> 150',
        'Gladius -> Heal -> 200',
        'Gladius -> Support -> 250',
        'Gladius -> Shield -> 250',
        'Peter vs Gladius',
        'Gladius vs Julius',
        'Gladius vs Maximilian',
        'Ave Cesar'
    ]
);

// Gladius: 700 skill
// - Shield <!> 250
// - Support <!> 250
// - Heal <!> 200
// Peter: 400 skill
// - Duck <!> 400
