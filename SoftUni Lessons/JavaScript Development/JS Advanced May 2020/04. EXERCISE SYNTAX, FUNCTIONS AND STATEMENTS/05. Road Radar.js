function roadRadar(input) {
    // Mask
    let speed = Number(input.shift());
    let area = input.shift();

    let limits = {
        motorway: 130,
        interstate: 90,
        city: 50,
        residential: 20,
    };

    let difference = speed - limits[area];
    
    if (difference > 0 && difference <= 20) {
        console.log('speeding');
    } else if (difference > 20 && difference <= 40) {
        console.log(`excessive speeding`);
    } else if (difference > 40) {
        console.log(`reckless driving`);
    }
}

roadRadar([40, 'city']);  // Should return:
roadRadar([21, 'residential']);  // Should return: speeding
roadRadar([120, 'interstate']);  // Should return: excessive speeding
roadRadar([200, 'motorway']);  // Should return: reckless driving
