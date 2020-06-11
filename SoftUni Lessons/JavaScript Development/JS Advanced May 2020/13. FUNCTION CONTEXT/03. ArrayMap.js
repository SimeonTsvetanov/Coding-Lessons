function arrayMap(array, func) {
    // this was mine solution:
    // let newArray = []; 
    // array.forEach(el => {
    //     newArray.push(func(el));
    // });
    // return newArray;

    // Solution in class:
    return array.reduce(function (acc, curr) {
        return acc.concat(func(curr));
    }, []);
}

let nums = [1,2,3,4,5];	
console.log(arrayMap(nums,(item)=> item * 2)); // [ 2, 4, 6, 8, 10 ]

let letters = ["a","b","c"];
console.log(arrayMap(letters,(l)=>l.toLocaleUpperCase())) // [ 'A', 'B', 'C' ]
