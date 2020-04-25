// push() – add to the end
// pop() – remove from the end
// unshift() – add to the beginning
// shift() – remove from the beginning
// slice() – remove a range of elements
// splice() – insert at position/delete from position

let mask = [1, 2, 3, 4, 5];

let poppedElement = mask.pop(); // removes the last element: 5 from the massive.
console.log(poppedElement);  // 5
console.log(mask); // [ 1, 2, 3, 4 ]

mask.push(5);  // Adds 5 to the end of the massive.
console.log(mask); // [ 1, 2, 3, 4, 5 ]

let shiftedElement = mask.shift() ;// Removes the first element: 1 of the massive.
console.log(shiftedElement);  // 1
console.log(mask); // [ 2, 3, 4, 5 ]

mask.unshift(1);  // Adds the element 1 a the beginning of the massive.
console.log(mask);  // [ 1, 2, 3, 4, 5 ]

cut = mask.slice(1, 3);  // It will cut the range of elements in the massive in the range of the given indexes.
console.log(cut);  // [ 2, 3 ]

mask.splice(1, 2);  // It will delete the element form the starting index 1 to the given count
console.log(mask);  // [ 1, 4, 5 ]

// IF we use the delete method it will only replace the value of the aimed element with undefined:
console.log(mask);  // [ 1, 4, 5 ]
delete mask[1];
console.log(mask);  // [ 1, <1 empty item>, 5 ]
// It's better to use shift() or pop() instead so we can remove the element.

// The slice() function returns a newly created array
// Gets a range of elements from selected start to end(exclusive)
// Note that the original array will not be modified
let a = [1, 2, 3, 4, 5, 6];
let slice = a.slice(2);  // Cuts the portion after the given index (inclusive) and returns a newly created array.
console.log(slice);  // [ 3, 4, 5, 6 ]
// We can cut using a range of elements:
let slicedRange = a.slice(1, 4);
console.log(slicedRange); // [ 2, 3, 4 ]

// The splice() adds/removes items to/from an array, and
// returns the removed item(s)
// This function changes the original array
let b = [1, 2, 3, 4, 5, 6];
let spliced = b.splice(2, 3)  // Start to Delete : Deleted Count
console.log(b);  // [ 1, 2, 6 ]  --> the original was changed !!!
console.log(spliced);  // [ 3, 4, 5 ]  --> The values Are now here...
b.splice(2, 3,3, 4, 5);
console.log(b);  // [ 1, 2, 3, 4, 5 ]