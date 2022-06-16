function townInfo (...args) {
    // MasK
    let city = args.shift();
    let population = args.shift();
    let area = args.shift();

    console.log(`Town ${city} has population of ${population} and area ${area} square km.`);
}

townInfo('Sofia', 123, 12);