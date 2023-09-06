function mask () {
    // MASK
    let a = [...Array(101).keys()].slice(1).forEach(x => {
        (x % 3 === 0) ? console.log(x) : 'pass';
    });
}

mask();
//
