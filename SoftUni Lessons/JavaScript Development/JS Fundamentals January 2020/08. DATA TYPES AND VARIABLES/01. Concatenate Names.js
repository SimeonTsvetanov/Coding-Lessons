function concatenateNames(first, last, delimeter) {
    // Mask
    console.log(`${first}${delimeter}${last}`);
}

concatenateNames('John', 'Smith', '->');  // Should return:
// John->Smith

concatenateNames('Jan', 'White', '<->');  // Should return:
// Jan<->White
