function projectCreation(input) {
    let name = input.shift();
    let projectsCount = Number(input.shift());
    let timeNeeded = projectsCount * 3;
    let message = `The architect ${name} will need ${timeNeeded} hours to complete ${projectsCount} project/s.`;
    console.log(message);
}

projectCreation(["George", 4]);
projectCreation(["Sonya", 9]);
