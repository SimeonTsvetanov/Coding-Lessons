function firstAndLastKNumbers(array) {
    // Mask
    // I have used Two different methods to solve the task
    // As you can see (hopefully) down bellow:

    let k = array.shift();  // --> Get the Count

    function methodLame(array) {
        let first = [];
        let last = [];
        for (let time = 0; time < k; time += 1) {
            first.push(array[time]);
            last.unshift(array[array.length - 1 - time]);
        }
        console.log(...first);  // --> Alternative to console.log(array.join(' '))
        console.log(...last);
    }

    function methodPro(array) {
        console.log(array.slice(0, k).join(' '));
        console.log(array.slice(array.length-k, array.length).join(' '));
    }

    // methodLame(array);
    methodPro(array);
}

firstAndLastKNumbers([2, 7, 8, 9]);  // Should return:
// 7 8
// 8 9

firstAndLastKNumbers([3, 6, 7, 8, 9]);  // Should return:
// 6 7 8
// 7 8 9
