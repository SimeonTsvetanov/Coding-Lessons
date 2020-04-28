function songs(input) {
    // Mask
    let playlist = [];  // Here we will keep all the songs


    class Song {
        // This is the constructor of the class
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    let numberOfSongs = Number(input.shift());  // The count of the songs

    for (let song = 1; song <= numberOfSongs; song += 1) {
        let [typeList, name, time] = input.shift().split('_');
        playlist.push(new Song(typeList, name, time));  // Append the song in the playlist
    }

    let typeOrAll = input.shift();  // the type to print.

    if (typeOrAll === 'all') {
        // Print all the Song names:

        // Simple Print:
        /*
        for (let song of playlist) {
            console.log(song.name);
        }
         */

        // Advanced Print:
        playlist.forEach((song) => console.log(song.name));
    } else {
        // WE need to print only the type required.

        // Simple print:
        /*
        for (let song of playlist) {
            song.typeList === typeOrAll ? console.log(song.name) : 'pass';
        }
         */

        // Advanced Print:
        let filtered = playlist.filter((song) => song.typeList === typeOrAll);
        filtered.forEach((song) => console.log(song.name));
    }
}

songs([3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite']
);
// Should return:
// DownTown
// Kiss
// Smooth Criminal

songs([4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'listenLater']
);
// Should return:
// Andalouse

songs([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']
);
// Should return:
// Replay
// Photoshop

