function sqareFrame(input) {
    // Mask     
    let n = Number(input.shift());

    let sqare = ""

    let frame = "+ ";
    for (i = 1; i <= (n - 2); i += 1) {
        frame += "- ";
    }
    frame += "+";
    
    sqare += `${frame}\n`

    for (i = 1; i <= (n - 2); i += 1) {
        let fill = "| ";
        for (j = 1; j <= (n - 2); j += 1) {
            fill += "- ";
        }   
        fill += "|";
        sqare += `${fill}\n`
    }
    sqare += `${frame}\n`

    console.log(sqare);
}       

sqareFrame([3]);  // Should return:
// + - +
// | - |
// + - +

sqareFrame([6]);  // Should return:
// + - - - - +
// | - - - - |
// | - - - - |
// | - - - - |
// | - - - - |
// + - - - - +
