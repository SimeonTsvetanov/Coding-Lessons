function projectCreation(name, projectsCount) {
    let timeNeeded = projectsCount * 3;
    let message = `The architect ${name} will need ${timeNeeded} hours to complete ${projectsCount} project/s.`;
    console.log(message);
}

projectCreation("George", 4);
projectCreation("Sonya", 9);
