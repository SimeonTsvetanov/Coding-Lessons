function songs (data) {
    // MasK
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }

        play = () => { console.log(this.name); }
    }

    class Music {
        constructor() {
            this.songs = [];
        }

        addSong = (song) => { this.songs.push(song); }

        play = (playlistOrAll) => {
            if (playlistOrAll === 'all') {
                this.songs.forEach(song => {song.play()});
            } else {
                this.songs.forEach(song => {
                    song.typeList === playlistOrAll ? song.play() : 'pass';
                });
            }
        }
    }

    let music = new Music();

    let songsCount = data.shift();
    for (let i = 0; i < songsCount; i++) {
        const [typeList, name, time] = data.shift().split('_');
        const song = new Song(typeList, name, time);
        music.addSong(song);
    }

    music.play(data.shift());
}

songs([3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite']
);
// DownTown
// Kiss
// Smooth Criminal

console.log('--------------');

songs([4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'listenLater']
);
// Andalouse
