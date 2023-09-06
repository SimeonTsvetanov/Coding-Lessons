function mask (...params) {
    // MASK
    const [first, last, del] = params;
    console.log(`${first}${del}${last}`);
}

mask('John',
'Smith'
,
'->'
);
// John->Smith

