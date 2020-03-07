function concatenateData(input) {
    let firstName = input.shift();
    let lastName = input.shift();
    let age = input.shift();
    let town = input.shift();

    let message = `You are ${firstName} ${lastName}, a ${age}-years old person from ${town}. `;
    console.log(message);
}

concatenateData(["Maria","Ivanova",20,"Sofia"]);
