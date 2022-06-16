// Write a program that receives a string of number n and print all triples of the first n small Latin letters, ordered alphabetically:

function triplets(n) {
    n = Number(n);
    let alphabet = 'abcdefghijklmnopqrstuvwxyz';
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            for (let k = 0; k < n; k++) {
                console.log(alphabet[i] + alphabet[j] + alphabet[k]);
            }
        }
    }
}

triplets('3');