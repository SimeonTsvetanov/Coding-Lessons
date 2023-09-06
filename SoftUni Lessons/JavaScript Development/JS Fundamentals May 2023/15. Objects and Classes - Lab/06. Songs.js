function mask (params) {
    // MASK
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = Number(time);
        }
    }

    let songs = [];

    let n = params.shift();
    for(let i = 0; i < n; i++) {
        let [typeList, name, time] = params.shift().split('_');
        songs.push(new Song(typeList, name, time));
    }

    let searched = params.shift();

    if (searched === 'all') {
        songs.forEach(song => {
            console.log(song.name);
        });
    } else {
        songs.forEach(song => {
            if (song.typeList === searched) {
                console.log(song.name);
            }
        });
    }
}

mask([3,
'favourite_DownTown_3:14',
'favourite_Kiss_4:16',
'favourite_Smooth Criminal_4:01',
'favourite']);
// DownTown
// Kiss
// Smooth Criminal

console.log('-------------------------------------');

mask([4,
'favourite_DownTown_3:14',
'listenLater_Andalouse_3:24',
'favourite_In To The Night_3:58',
'favourite_Live It Up_3:48',
'listenLater']);
// Andalouse

