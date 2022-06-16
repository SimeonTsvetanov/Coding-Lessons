function gramophone(name, album, song) {
    let songDuration = (album.length * name.length) * song.length / 2;
    console.log(`The plate was rotated ${Math.ceil(songDuration / 2.5)} times.`);
}


gramophone('Black Sabbath', 'Paranoid', 'War Pigs');
