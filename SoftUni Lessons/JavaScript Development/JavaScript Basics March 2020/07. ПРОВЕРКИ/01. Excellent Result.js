// There are two ways of reading the Input for this tasks:
// This is the new way:
function excellentResult(mark) {
    if (mark >= 5.50) {
        console.log("Excellent!");
    }
}

excellentResult(6);  // Expected output: Excellent!
excellentResult(5); // Expected output: (няма изход)
excellentResult(5.50);  // Expected output: Excellent!
excellentResult(5.49);  // Expected output: (няма изход)


// -----------------------------------------------------------------------//
// This is the old way of reading the input:
function excellentResultOld(input) {
    mark = Number(input);
    if (mark >= 5.50) {
        console.log("Excellent!");
    }
}

excellentResultOld(['6']);  // Expected output: Excellent!
excellentResultOld(['5']); // Expected output: (няма изход)
excellentResultOld(['5.50']);  // Expected output: Excellent!
excellentResultOld(['5.49']);  // Expected output: (няма изход)
