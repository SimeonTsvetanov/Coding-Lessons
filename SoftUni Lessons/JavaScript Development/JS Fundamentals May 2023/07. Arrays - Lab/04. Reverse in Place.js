function mask (params) {
    // MASK
    console.log(params.reverse().join(' '));
}

mask(['a', 'b', 'c', 'd', 'e']);
// e d c b a

mask(['abc', 'def', 'hig', 'klm', 'nop']);
// nop klm hig def abc
