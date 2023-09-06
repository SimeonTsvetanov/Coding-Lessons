function mask (params) {
    // MASK
    const year = params;

    let leap = 'no';

    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
        leap = 'yes';
    }

    console.log(leap);
}

mask(1984);
// yes

mask(2003);
// no
