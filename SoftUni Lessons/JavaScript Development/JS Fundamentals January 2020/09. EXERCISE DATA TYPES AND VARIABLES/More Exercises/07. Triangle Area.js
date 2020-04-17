function triangleArea(a, b, c) {
    // Mask
    let s = (a + b + c) / 2;
    area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    console.log(area);
}

triangleArea(2, 3.5, 4);  // Should return: 3.4994419198
