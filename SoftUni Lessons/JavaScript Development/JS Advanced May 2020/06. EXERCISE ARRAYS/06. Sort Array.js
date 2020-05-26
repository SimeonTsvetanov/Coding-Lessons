function sortArray(array) {
    // Mask - https://git.io/JfwFw
    array.sort(function (a, b) {
        return a.length - b.length || a.localeCompare(b);
    });
    console.log(array.join('\n'));
}

sortArray(['alpha', 'beta', 'gamma']);
// Should return:
// beta
// alpha
// gamma

sortArray(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George']);
// Should return:
// Jack
// Isacc
// George
// Theodor
// Harrison
