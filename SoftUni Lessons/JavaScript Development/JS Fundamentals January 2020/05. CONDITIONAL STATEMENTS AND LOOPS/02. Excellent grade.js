function excellentGrade(num) {
    // Mask
    if (num >= 5.5) {
        console.log('Excellent');
    } else {
        console.log('Not excellent');
    }
}

excellentGrade(5.50);  // Should return: Excellent

excellentGrade(4.35);  // Should return: Not excellent