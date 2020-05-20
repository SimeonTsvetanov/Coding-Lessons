function greatestCommonDicisor(one, two) {
    // Mask
    for (let i = Math.max(one, two); i >= 0; i--) {
        if (one % i === 0 && two % i === 0) {
            console.log(i);
            break;
        }
    }    
}

greatestCommonDicisor(15, 5);  // Should return: 5 

greatestCommonDicisor(2154, 458);  // Should return: 2
