function movieDay(params) {
    let timePictures = Number(params.shift());
    let countScenes = Number(params.shift());
    let timeScene = Number(params.shift());

    let actualTime = (timePictures * 0.15) + (countScenes * timeScene); 
    
    if (actualTime <= timePictures) {
        console.log(`You managed to finish the movie on time! You have ${Math.round(timePictures - actualTime)} minutes left!`);
    } else {
        console.log(`Time is up! To complete the movie you need ${Math.round(actualTime - timePictures)} minutes.`);
    }
}


movieDay(['120', '10', '11']);  // Expected Output:
// Time is up! To complete the movie you need 8 minutes.

movieDay(['60', '15', '3']);  // Expected Output:
// Time is up! To complete the movie you need 8 minutes.
