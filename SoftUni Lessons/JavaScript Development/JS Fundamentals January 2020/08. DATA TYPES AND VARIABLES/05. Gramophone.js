function gramophone(band, album, song) {
    // Mask
    let rotations = Math.ceil(((album.length * band.length) * song.length / 2) / 2.5);
    console.log(`The plate was rotated ${rotations} times.`);
}

gramophone('Black Sabbath', 'Paranoid', 'War Pigs');  // Should return:
// The plate was rotated 167 times.
