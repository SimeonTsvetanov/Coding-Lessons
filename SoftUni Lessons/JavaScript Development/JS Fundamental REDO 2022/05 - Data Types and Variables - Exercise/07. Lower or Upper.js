function lowerOrUpperCase (...args) {
    // MasK
    const isUpperCase = (string) => /^[A-Z]*$/.test(string)
    isUpperCase(args.shift()) ? console.log('upper-case') : console.log('lower-case');
}

lowerOrUpperCase('a');