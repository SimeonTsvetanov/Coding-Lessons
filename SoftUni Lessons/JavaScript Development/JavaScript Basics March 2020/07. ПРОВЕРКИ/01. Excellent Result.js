function excellentResult(input) {
    mark = Number(input);
    if (mark >= 5.50) {
        console.log("Excellent!");
    }
}

excellentResult(['6']);  // Expected output: Excellent!
excellentResult(['5']); // Expected output: (няма изход)
excellentResult(['5.50']);  // Expected output: Excellent!
excellentResult(['5.49']);  // Expected output: (няма изход)
