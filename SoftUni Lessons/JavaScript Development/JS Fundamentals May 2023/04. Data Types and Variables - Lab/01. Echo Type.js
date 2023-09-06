function mask (params) {
    // MASK
    const data = params;
    const type = typeof(data);
    console.log(type);
    (['string', 'number'].includes(type)) ? console.log(data) : console.log('Parameter is not suitable for printing')
}

mask('Hello, JavaScript!');
// string
// Hello, JavaScript!

mask(18);
// number
// 18

mask(null);
// object
// Parameter is not suitable for printing
