function market(input) {
    let whiskeyPrice = input.shift();
    let beerLiters = input.shift();
    let wineLiters = input.shift();
    let rakiaLiters = input.shift();
    let whiskeyLiters = input.shift();

    let whiskeyTotal = whiskeyPrice * whiskeyLiters;
    let rakiaTotal = (whiskeyPrice / 2) * rakiaLiters;
    let wineTotal = ((whiskeyPrice / 2) * 0.6) * wineLiters;
    let beerTotal = ((whiskeyPrice / 2) * 0.2) * beerLiters;

    let total = (whiskeyTotal + rakiaTotal + wineTotal + beerTotal).toFixed(2);
    console.log(total);
}

market([50, 10, 3.5, 6.5, 1]);  // Expected Output: 315.00
market([63.44, 3.57, 6.35, 8.15, 2.5]);  // Expected Output: 560.62
