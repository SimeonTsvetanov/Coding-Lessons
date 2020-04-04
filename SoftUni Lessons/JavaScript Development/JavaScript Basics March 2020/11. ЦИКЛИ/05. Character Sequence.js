// I have added two different methods for solving this task.

function characterSquenceONE(...params) {
    word = params.shift();
    for (let letter of word) {
        console.log(letter);
    }
}

function characterSquenceTWO(params) {
    let word = params.shift();
    let length = word.length;
    for (i = 0; i < length; i++) {
        console.log(word[i])
    }
}


characterSquenceTWO('Softuni');
