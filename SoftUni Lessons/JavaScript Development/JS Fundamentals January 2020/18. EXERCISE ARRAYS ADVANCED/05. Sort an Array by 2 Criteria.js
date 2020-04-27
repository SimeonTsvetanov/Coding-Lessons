function sortAnArrayByTwoCriteria(array) {
    // Mask
    array.sort(function (a, b) {
        return a.length - b.length || a.localeCompare(b);
    });
    console.log(array.join('\n'));
}

sortAnArrayByTwoCriteria(["alpha", "beta", "gamma"]);
// Should return:
// beta
// alpha
// gamma

sortAnArrayByTwoCriteria(["Isacc", "Theodor", "Jack", "Harrison", "George"]);
// Should return:
// Jack
// Isacc
// George
// Theodor
// Harrison
