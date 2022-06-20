function charsInRange (a, b) {
    // MasK
    [a, b] = [a.charCodeAt(0), b.charCodeAt(0)].sort((a, b) => a - b);
    let result = [];
    for (let char = a + 1; char < b; char++) {
        result.push(String.fromCharCode(char))
    }
    console.log(result.join(' '));
}

charsInRange('C', '#');  // $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B