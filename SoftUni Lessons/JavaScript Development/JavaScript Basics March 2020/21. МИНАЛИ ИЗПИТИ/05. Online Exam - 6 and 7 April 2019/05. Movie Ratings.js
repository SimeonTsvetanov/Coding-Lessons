function movieRatings(input) {
    // Mask
    let count = Number(input.shift());
    
    let bestRatedName = '';
    let bestRating = Number.MIN_SAFE_INTEGER;
    let worstRatedName = '';
    let worstRating = Number.MAX_SAFE_INTEGER;
    let totalScores = 0;

    for(let movie = 1; movie <= count; movie += 1) {
        let name = input.shift();
        let rating = Number(input.shift());

        if (rating > bestRating) {
            bestRatedName = name;
            bestRating = rating;
        }

        if (rating < worstRating) {
            worstRatedName = name;
            worstRating = rating;
        }
    
        totalScores += rating;
    }

    console.log(`${bestRatedName} is with highest rating: ${bestRating.toFixed(1)}`);
    console.log(`${worstRatedName} is with lowest rating: ${worstRating.toFixed(1)}`);
    console.log(`Average rating: ${(totalScores / count).toFixed(1)}`);
}

movieRatings([5, 'A Star is Born', 7.8, 'Creed 2', 7.3, 'Mary Poppins', 7.2, 'Vice', 7.2, 'Captain Marvel', 7.1]);  
// Should return:
// A Star is Born is with highest rating: 7.8
// Captain Marvel is with lowest rating: 7.1
// Average rating: 7.3

movieRatings([3, 'Interstellar', 8.5, 'Dangal', 8.3, 'Green Book', 8.2]);  
// Should return:
// Interstellar is with highest rating: 8.5
// Green Book is with lowest rating: 8.2
// Average rating: 8.3
