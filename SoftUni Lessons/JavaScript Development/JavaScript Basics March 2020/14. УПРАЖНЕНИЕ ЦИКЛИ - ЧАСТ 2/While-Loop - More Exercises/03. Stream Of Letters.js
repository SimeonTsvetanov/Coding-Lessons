// Just remember, this task has taken 1.5 bloody hours of my life.
// So be caferfull with it :D

function streamOfLetters(params) {
    let letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    let c = false;
    let o = false;
    let n = false;

    let masterSecret = '';
    let secret = ''

    while ("I say so!") {
        if (c && o && n) {
            secret += ' ';
            masterSecret += secret;
            secret = ''
            c = false;
            o = false;
            n = false;
        }
        let letter = params.shift();
        if (letter == 'End') {break;}
        if (letters.includes(letter)) {
            if (!(c && o && n)) {
                if (letter == 'c' && !(c)) {
                    c = true;
                } else if (letter == 'c'){
                    secret += letter;
                }
    
                else if (letter == 'o' && !(o)) {
                    o = true;
                } else if (letter == 'o') {
                    secret += letter;
                }
    
                else if (letter == 'n' && !(n)) {
                    n = true;
                } else if (letter == 'n') {
                    secret += letter;
                }
    
                else {
                    secret += letter;
                }
            }
        }
    }

    console.log(masterSecret);
}

streamOfLetters(['H', 'n', 'e', 'l', 'l', 'o', 'o', 'c', 't', 'c', 'h', 'o', 'e', 'r', 'e', 'n', 'e', 'End']);
// Expected Output: Hello there