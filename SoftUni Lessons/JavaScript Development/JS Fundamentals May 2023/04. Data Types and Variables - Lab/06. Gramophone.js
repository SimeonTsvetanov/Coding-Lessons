function mask (...params) {
    // MASK
    const [band, album, song] = params;

    const duration = (album.length * band.length) * song.length / 2;
    const rotations = Math.ceil(duration / 2.5);
    console.log(`The plate was rotated ${rotations} times.`);
}

mask('Black Sabbath', 'Paranoid',
'War Pigs');
// The plate was rotated 167 times.

mask('Rammstein', 'Sehnsucht',
'Engel');
// The plate was rotated 81 times.
