function echoType(value) {
    const type = typeof value;
    console.log(type);
    ['string', 'number'].includes(type) ? console.log(value) : console.log('Parameter is not suitable for printing');
}

echoType('mask');
echoType(1);
echoType(1.1);
echoType(true);
