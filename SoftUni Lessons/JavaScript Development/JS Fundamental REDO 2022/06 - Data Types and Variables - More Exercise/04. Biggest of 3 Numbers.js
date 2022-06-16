function biggestOfTreeNumbers (...args) {
    let biggest = Math.max.apply(null, args);
    console.log(biggest);
}

biggestOfTreeNumbers(-2, 7, 3);