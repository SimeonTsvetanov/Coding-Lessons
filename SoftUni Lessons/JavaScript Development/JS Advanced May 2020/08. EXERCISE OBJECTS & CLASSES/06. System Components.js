function systemComponents(input) {
    // Mask - https://git.io/JfreH
    let systems = {};

    input.map(data => {
        let [systemName, componentName, subComponentName] = data.split(' | ');

        !systems.hasOwnProperty(systemName) ? systems[systemName] = {} : 'pass';
        !systems[systemName].hasOwnProperty(componentName)
            ? systems[systemName][componentName] = [subComponentName]
            : systems[systemName][componentName].push(subComponentName);
    });

    for (let system of Object.keys(systems).sort((a, b) =>
        {return Object.keys(systems[b]).length - Object.keys(systems[a]).length || a.localeCompare(b)})) {
        console.log(system);
        for (let component of Object.keys(systems[system]).sort((a, b) =>
            systems[system][b].length - systems[system][a].length)) {
            console.log(`|||${component}`);
            for (let subComponent of systems[system][component]) {
                console.log(`||||||${subComponent}`);
            }
        }
    }
}

systemComponents([
    'SULS | Main Site | Home Page',
    'SULS | Main Site | Login Page',
    'SULS | Main Site | Register Page',
    'SULS | Judge Site | Login Page',
    'SULS | Judge Site | Submittion Page',
    'Lambda | CoreA | A23',
    'SULS | Digital Site | Login Page',
    'Lambda | CoreB | B24',
    'Lambda | CoreA | A24',
    'Lambda | CoreA | A25',
    'Lambda | CoreC | C4',
    'Indice | Session | Default Storage',
    'Indice | Session | Default Security'
]);  // Should return:
// Lambda
// |||CoreA
// ||||||A23
// ||||||A24
// ||||||A25
// |||CoreB
// ||||||B24
// |||CoreC
// ||||||C4
// SULS
// |||Main Site
// ||||||Home Page
// ||||||Login Page
// ||||||Register Page
// |||Judge Site
// ||||||Login Page
// ||||||Submittion Page
// |||Digital Site
// ||||||Login Page
// Indice
// |||Session
// ||||||Default Storage
// ||||||Default Security
