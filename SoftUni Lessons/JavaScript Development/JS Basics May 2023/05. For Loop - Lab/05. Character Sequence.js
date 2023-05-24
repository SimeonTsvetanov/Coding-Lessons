function characters(params) {
    params.shift().split('').forEach(letter => {
        console.log(letter);
    });
}

characters(["softuni"]);
