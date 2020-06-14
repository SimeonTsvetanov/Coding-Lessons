// let solution = (function () {
//     let number = 0;
//     return function (value) {number += value; return number}
// })();
// This code doesn't go in Judge...
// console.log(solution(5));  // => 5
// console.log(solution(5));  // => 10
// console.log(solution(5));  // => 15
function solution(num1) {
    let num3 = 0;
    return function (num2) {
        num3 = num1 + num2;
        return num3
    }
}

let add5 = solution(5);
console.log(add5(2));  // => 7
console.log(add5(3));  // => 8

