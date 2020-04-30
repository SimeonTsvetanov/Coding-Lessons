function movies(data) {
    // Mask
    let allMovies = [];

    for (let command of data) {
        let details = command.split(' ');
        if (details[0] === "addMovie") {
            details.shift();
            let name = (details.join(' '));
            allMovies.push({name: name});
        } else {
            if (command.includes('directedBy')) {
                let name = command.split(' directedBy ')[0];
                let director = command.split(' directedBy ')[1];
                allMovies.map((movie) => {
                    movie.name === name ? movie['director'] = director : 'pass'
                })

            } else {
                let name = command.split(' onDate ')[0];
                let date = command.split(' onDate ')[1];
                allMovies.map((movie) => {
                    movie.name === name ? movie['date'] = date : 'pass'
                })
            }
        }
    }

    allMovies.map((movie) => {
        if (movie.name && movie.director && movie.date) {
            console.log(JSON.stringify(movie))
        }
    });
}

movies([
        'addMovie Fast and Furious',
        'addMovie Godfather',
        'Inception directedBy Christopher Nolan',
        'Godfather directedBy Francis Ford Coppola',
        'Godfather onDate 29.07.2018',
        'Fast and Furious onDate 30.07.2018',
        'Batman onDate 01.08.2018',
        'Fast and Furious directedBy Rob Cohen'
    ]
);  // Should return:
// {"name":"Fast and Furious","date":"30.07.2018","director":"Rob Cohen"}
// {"name":"Godfather","director":"Francis Ford Coppola","date":"29.07.2018"}
