function triangleArea (...args) {
    const side1 = args.shift();
    const side2 = args.shift();
    const side3 = args.shift();
    const s = (side1 + side2 + side3) / 2;
    const area =  Math. sqrt(s * ((s - side1) * (s - side2) * (s - side3)));
    console.log(area);
}

triangleArea(2,
    3.5,
    4
);