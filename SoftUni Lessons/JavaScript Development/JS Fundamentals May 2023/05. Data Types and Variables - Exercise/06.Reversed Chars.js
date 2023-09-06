function mask (...params) {
    // MASK
    console.log(params.reverse().join(' '))
}

mask('A',
'B',
'C');
// C B A

mask('1',
'L',
'&');
// & L 1
