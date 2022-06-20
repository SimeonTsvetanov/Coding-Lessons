function steamAccount (data)  {
    // MasK
    let games = data.shift().split(' ');

    while ('you receive "Play!') {
        let [command, game] = data.shift().split(' ');

        if (command === 'Play!') {
            break;
        } else if (command === 'Install') {
            !games.includes(game) ? games.push(game) : 'already included';
        } else if (command === 'Uninstall') {
            if (games.includes(game)) {
                let index = games.indexOf(game);
                games.splice(index, 1);
            }
        } else if (command === 'Update') {
            if (games.includes(game)) {
                let index = games.indexOf(game);  // get the index
                games.splice(index, 1);  // remove it from the array
                games.push(game);  // place it on the last position
            }
        } else if (command === 'Expansion') {
            let [gameName, ext] = game.split('-')
            if (games.includes(gameName)) {
                let index = games.indexOf(gameName);  // get the index
                games.splice(index + 1, 0, `${gameName}:${ext}`);
            }
        }

    }

    console.log(games.join(' '));
}


steamAccount(['CS WoW Diablo',
    'Install LoL',
    'Uninstall WoW',
    'Update Diablo',
    'Expansion CS-Go',
    'Play!']
);  // CS CS:Go LoL Diablo


steamAccount(['CS WoW Diablo',
    'Uninstall XCOM',
    'Update PeshoGame',
    'Update WoW',
    'Expansion Civ-V',
    'Play!']
);  // CS Diablo WoW