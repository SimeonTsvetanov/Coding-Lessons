"use strict";
//  (not included in final score)

function wordsUppercase(input) {
    // Mask
    let results = String(input.match(/(\w|\s)*\w(?=")|\w+/g)).toUpperCase().split(",");
    console.log(results.join(', '));
}

wordsUppercase('Hi, how are you?');  // Should return:
// HI, HOW, ARE, YOU

wordsUppercase('hello');  // Should return:
// HELLO
