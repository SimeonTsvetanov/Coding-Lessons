// I have a few ways to solve this taks.

function vowelsSumONE(...params) {
    let word = params.shift();

    let points = {
        'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5
    };

    let total = 0;

    for (let letter of word) {
        if (points[letter]) {
            total += points[letter]
        }
    }

    console.log(total);    
}

// Secon option is from the presentation:
function vowelsSumTWO(...params) {
    let word = params.shift();

    let total = 0

    for (let i = 0; i <= word.length; i++) {
        switch (word[i]) {
            case 'a': total += 1; break;
            case 'e': total += 2; break;
            case 'i': total += 3; break;
            case 'o': total += 4; break;
            case 'u': total += 5; break;
        }
    }

    console.log(total);    
}

vowelsSumTWO('bamboo');
