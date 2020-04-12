function lettersCombinations(input) {
    // Mask
    // How Does ASCII works:
    
    // 'A'.charCodeAt(0)        --> Will return the digit 65
    // String.fromCharCode(65)  --> Will return the letter A
    
    let start = input.shift();
    let end = input.shift();
    let skip = input.shift();

    let result = ''  // here we keep the final result
    let count = 0  // Keeps the count of the valid combinations

    // Now to get 3 combinations we need 
    // 3 for loops ALL THE SAME from Start to End:    

    for (x1 = start.charCodeAt(0); x1 <= end.charCodeAt(0); x1 += 1) {  // x1 is the first letter
        for (x2 = start.charCodeAt(0); x2 <= end.charCodeAt(0); x2 += 1) {  // x2 is the second letter
            for (x3 = start.charCodeAt(0); x3 <= end.charCodeAt(0); x3 += 1) {  // x3 is the third letter
                let current = `${String.fromCharCode(x1)}${String.fromCharCode(x2)}${String.fromCharCode(x3)} `
                if (!current.includes(skip)) {
                    // So We don't have the skip letter 
                    // And we can append the current to the result
                    result += current;
                    count += 1; // update the count :)
                }
            }
        }
    }

    result += count;  // add the count to the end of the result
    console.log(result); // And log it.
}

lettersCombinations(['a', 'c', 'b']);  // Should return:
// aaa aac aca acc caa cac cca ccc 8

console.log() // Added empty line for better readability!

lettersCombinations(['a', 'c', 'z']);  // Should return:
// aaa aab aac aba abb abc aca acb acc baa bab bac bba bbb bbc bca bcb bcc caa cab cac cba cbb cbc cca ccb ccc 27