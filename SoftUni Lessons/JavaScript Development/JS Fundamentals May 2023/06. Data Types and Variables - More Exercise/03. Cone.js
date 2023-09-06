function mask (...params) {
    // MASK
    const [radius, height] = params;
    const slant = Math.sqrt(radius * radius + height * height);
    const volume = (Math.PI * radius ** 2 * height / 3.0);
    const area = Math.PI * radius * (radius + slant);

    console.log(`volume = ${volume.toFixed(4)}`);
    console.log(`area = ${area.toFixed(4)}`);
}

mask(3,
5);
// volume = 47.1239
// area = 83.2298

mask(3.3,
7.8);
// volume = 88.9511
// area = 122.0159
