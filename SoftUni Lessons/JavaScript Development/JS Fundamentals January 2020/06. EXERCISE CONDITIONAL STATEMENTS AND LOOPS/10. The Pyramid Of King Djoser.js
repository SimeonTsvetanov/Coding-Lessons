// (not included in final score)

function thePyramidOfKingDjoser(base, increment) {
    // Mask
    let totalstone = 0;
    let totalmarble = 0;
    let totallapis = 0;
    let totalgold = 0;
    let row = 0;
    let currentbase=base;
 
    while (currentbase > 2) {
     let marbel = currentbase * 4 - 4;
     let stone = currentbase * currentbase - marbel;
        totalstone += stone;
 
        row += 1;
        if(row % 5 == 0) {
            totallapis += marbel;
        } else {
            totalmarble += marbel;
        }
        currentbase -= 2;
    }
    row += 1;
    let gold = currentbase * currentbase;
   
    stone = Math.ceil(totalstone * increment);
    marble = Math.ceil(totalmarble * increment);
    lapis = Math.ceil(totallapis * increment);
    totalgold = Math.ceil(gold * increment);
    totalHeight = Math.floor(row * increment);
 
    console.log(`Stone required: ${stone}`);
    console.log(`Marble required: ${marble}`);
    console.log(`Lapis Lazuli required: ${lapis}`);
    console.log(`Gold required: ${totalgold}`);
    console.log(`Final pyramid height: ${totalHeight}`);
}

thePyramidOfKingDjoser(11, 1);  // Should return:
// Stone required: 165
// Marble required: 112
// Lapis Lazuli required: 8
// Gold required: 1
// Final pyramid height: 6


thePyramidOfKingDjoser(11, 0.75);  // Should return:
// Stone required: 124
// Marble required: 84
// Lapis Lazuli required: 6
// Gold required: 1
// Final pyramid height: 4
