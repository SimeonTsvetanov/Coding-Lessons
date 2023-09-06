function mask (language) {
    // MASK
    if (['England', 'USA'].includes(language)) {
        console.log('English');
    } else if (['Spain', 'Argentina', 'Mexico'].includes(language)) {
        console.log('Spanish')
    } else {
        console.log('unknown')
    }
}

mask("USA");
// English

mask("Germany");
// unknown
