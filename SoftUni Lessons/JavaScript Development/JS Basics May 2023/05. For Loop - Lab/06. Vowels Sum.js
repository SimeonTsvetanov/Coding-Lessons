function vowelsSum(params) {
    let delta = {
        "a": 1,
        "e": 2,
        "i": 3,
        "o": 4,
        "u": 5,
    }

    let result = 0;

    params.shift().split("").forEach((letter, index) => {
        (letter in delta) ? result += delta[letter] : 'pass';
    });
    
    console.log(result);
}

vowelsSum((["hello"]));  // 6
vowelsSum((["hi"]));  // 3
vowelsSum((["bamboo"]));  // 9
