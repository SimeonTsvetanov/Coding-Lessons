function charactersInRange(a, b) {
    // Mask
    let result = [];

    for (let char = Math.min(a.charCodeAt(0), b.charCodeAt(0)) + 1; char < Math.max(a.charCodeAt(0), b.charCodeAt(0)); char += 1) {
        result.push(String.fromCharCode(char));
    }

    console.log(...result);
}

charactersInRange('#', ':');
// Should return: $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9

charactersInRange('C', '#');
// Should return: b c
