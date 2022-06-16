function rightPlace(stringOne, char, stringTwo) {
    stringOne.replace('_', char) === stringTwo ? console.log('Matched') : console.log('Not Matched');
}

rightPlace('_Hi_there_', '!', 'Bye!');
rightPlace('Str_ng', 'i', 'String');
