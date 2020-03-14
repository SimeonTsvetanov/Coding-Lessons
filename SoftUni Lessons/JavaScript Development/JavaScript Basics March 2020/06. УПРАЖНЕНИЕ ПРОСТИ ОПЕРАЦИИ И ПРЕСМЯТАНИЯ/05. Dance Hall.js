// There is new way to read the input, so I will include it here, but,
// If you wish to check the old ways still: it's down bellow.
function danceHall(length, width, wardrobeSide) {
    let hallsSizeSquareCm = (length * 100) * (width * 100);
    let wardrobeSizeSqareCm = (wardrobeSide * 100) * (wardrobeSide * 100);
    let benchSizeSqareCm = hallsSizeSquareCm / 10;

    let freeSpace = hallsSizeSquareCm - wardrobeSizeSqareCm - benchSizeSqareCm;
    let dancers = Math.floor(freeSpace / (40 + 7000));
    console.log(dancers);
}   
danceHall(50, 25, 2);  // Expected output: 1592


// This was the old way of reading the Input:
function danceHallOld(input) {
    let length = Number(input.shift());
    let width = Number(input.shift());
    let wardrobeSide = Number(input.shift());

    let hallsSizeSquareCm = (length * 100) * (width * 100);
    let wardrobeSizeSqareCm = (wardrobeSide * 100) * (wardrobeSide * 100);
    let benchSizeSqareCm = hallsSizeSquareCm / 10;

    let freeSpace = hallsSizeSquareCm - wardrobeSizeSqareCm - benchSizeSqareCm;
    let dancers = Math.floor(freeSpace / (40 + 7000));
    console.log(dancers);
}   

danceHallOld(["50", "25", "2"]);  // Expected output: 1592
