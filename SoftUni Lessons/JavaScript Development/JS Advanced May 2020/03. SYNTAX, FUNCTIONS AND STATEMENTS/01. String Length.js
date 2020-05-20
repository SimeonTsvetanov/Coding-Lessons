function stringLength(one, two, three) {
    // Mask
    let sum = one.length + two.length + three.length;
    let average = Math.floor(sum / 3);
    console.log(sum);
    console.log(average);
}

stringLength('chocolate', 'ice cream', 'cake');  // Should return:
// 22
// 7

stringLength('pasta', '5', '22.3');  // Should return:
// 10
// 3