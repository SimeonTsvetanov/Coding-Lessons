function seriesCalculator(params) {
    let name = params.shift();
    let seasons = Number(params.shift());
    let episodes = Number(params.shift());
    let time = Number(params.shift()) * 1.2;

    let minutes = Math.floor((seasons * episodes * time) + (seasons * 10)); 
    console.log(`Total time needed to watch the ${name} series is ${minutes} minutes.`);
}


seriesCalculator(['Lucifer', '3', '18', '55']);  // Expected Output:
// Total time needed to watch the Lucifer series is 3594 minutes.

seriesCalculator(['Game of Thrones', '7', '10', '50']);  // Expected Output:
// Total time needed to watch the Game of Thrones series is 4270 minutes.

seriesCalculator(['Riverdale', '3', '21', '45']);  // Expected Output:
// Total time needed to watch the Riverdale series is 3432 minutes.