function ReadText(params) {
    
    let input = params.shift();
    while (input != 'Stop') {
        input = params.shift();
    }
}

ReadText(['Nakov', 'SoftUni', 'Sofia', 'Bulgaria', 'SomeText', 'Stop']);
