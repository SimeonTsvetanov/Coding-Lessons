function movies (data) {
    // MasK
    let movies = [];

    data.forEach(command => {
        if (command.includes('addMovie')) {
            let movie = command.split('addMovie ')[1];
            movies.push({name: movie});
        } else if (command.includes('directedBy')) {
            let [name, director] = command.split(' directedBy ');
            let movie = movies.find(obj => {
                return obj.name === name;
            });
            movie ? movie.director = director : 'pass';
        } else if (command.includes('onDate')) {
            let [name, date] = command.split(' onDate ');
            let movie = movies.find(obj => {
                return obj.name === name;
            });
            movie ? movie.date = date : 'pass';
        }
    });

    movies.forEach(movie => {
        if ('date' in movie && 'director' in movie) {
            console.log(JSON.stringify(movie));
        }
    });
}

movies([
        'addMovie Fast and Furious',
        'addMovie Godfather',
        'addMovie Godfather2',
        'Inception directedBy Christopher Nolan',
        'Godfather directedBy Francis Ford Coppola',
        'Godfather onDate 29.07.2018',
        'Fast and Furious onDate 30.07.2018',
        'Batman onDate 01.08.2018',
        'Fast and Furious directedBy Rob Cohen'
    ]
);

// {"name":"Fast and Furious","date":"30.07.2018","director":"Rob Cohen"}
// {"name":"Godfather","director":"Francis Ford Coppola","date":"29.07.2018"}