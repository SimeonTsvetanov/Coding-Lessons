function sortByTwoCriteria (array) {
    // MasK
    array.sort(
        function(a, b) {
            if (a.length === b.length) {
                // Second Criteria
                return a.toLowerCase().localeCompare(b.toLowerCase());
            }
            // Main Criteria
            return a.length - b.length;
        });

    console.log(array.join('\n'));
}

sortByTwoCriteria(['alpha', 'beta', 'gamma']);
// beta
// alpha
// gamma

sortByTwoCriteria(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George']);
// Jack
// Isacc
// George
// Theodor
// Harrison