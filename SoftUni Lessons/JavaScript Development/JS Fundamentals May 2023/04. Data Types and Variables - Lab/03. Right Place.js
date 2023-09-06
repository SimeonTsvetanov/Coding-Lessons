function mask (...params) {
    // MASK
    let [a, c, b] = params;
    (a.replace('_', c) === b) ? console.log(`Matched`) : console.log(`Not Matched`);
}

mask('Str_ng', 'I',
'Strong');
// Not Matched

mask('Str_ng', 'i',
'String' );
// Matched
