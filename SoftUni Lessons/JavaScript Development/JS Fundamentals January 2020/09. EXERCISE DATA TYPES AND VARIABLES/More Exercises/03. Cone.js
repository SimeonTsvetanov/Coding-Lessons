function cone(radius, height) {
    // Mask
    let side = Math.sqrt(radius * radius + height * height);
    let volume = Math.PI * radius * radius * height / 3;
    let area = Math.PI * radius * (radius + side);

    console.log(`volume = ${volume.toFixed(4)}`);
    console.log(`area = ${area.toFixed(4)}`);
}

cone(3, 5);  // Should return:
// volume = 47.1239
// area = 83.2298

cone(3.3, 7.8);  // Should return:
// volume = 88.9511
// area = 122.0159
