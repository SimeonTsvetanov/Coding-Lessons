//-----------------------------------------------------------//
//                 First- Class Function:                    //
//-----------------------------------------------------------//

//-----------------------------------------------------------//
// Functions can be passed as an argument to another function:
function sayHello() {
    // return 'Hello, '; // <-- Normal way of return

    // Also functions can be returned by another function
    // - We can do that, because we treated functions in JS as a value:
    return function () {
        return 'Hello';
    }
}

function greeting(helloMessage, name) {
    return helloMessage() + name;
}

// console.log(greeting(sayHello, 'JS Sucks!'));  // --> Hello, JS Sucks!


//-----------------------------------------------------------//
// Functions Can be assigned as a value to a variable:
const sayTheTruth = function() {
    return "Python is way better than JS!"
};
// In order to INVOKE the variable we need to call it with parentheses "()" at the end: 
// console.log(sayTheTruth());

//-----------------------------------------------------------//
// Predicates:
// - Any function that returns a bool (true/ false)...
// - They are often found in the form of callbacks:
let array1 = [1, 2, 3, 4, 5, 20, 6, 12];
let found = array1.find(isFound); // It will return the first found element in the array.
function isFound(element) {
    return element > 10; // true or false
}
// console.log(found); // 20

//-----------------------------------------------------------//
// Build in Higher -Order -Functions:
// => Array.prototype.map
// => Array.prototype.filter
// => Array.prototype.reduce
let users = [ { name: 'Time', age: 25}, { name: 'Sam', age: 30 }, { name: 'Bill', age: 20 } ];
let getName = (user) => user.name; // if given user object it will return it's name ONLY!
let usernames = users.map(getName);
// console.log(usernames); // [ 'Time', 'Sam', 'Bill' ]


//-----------------------------------------------------------//
// Pure Functions:
// Returns the same result given same parameters:
// It's execution doesnt depend on the state of the system:

// impure function:
let number = 1;
const increment = () => number + 1;
increment();  // 2

// pure function:
const pureIncrement = n => n + 1;
pureIncrement(1); // 2

//-----------------------------------------------------------//
// Referential Transparency:
// An expression that can be replaced with it's corresponding
// value without changing the program's behavior
// Expression is pure and it's evaluation must have no side Effects:

// referentially transparent functions:
function add(a, b) { return a + b; }
function multiplication(a, b) { return a * b; }
let x = add(2, multiplication(3, 4));//multiplication(3, 4)) can be replaced with 12
// console.log(x);

// not referentially transparent function:
function addTransparent(a, b) {
    let result = a + b;
    console.log("Returning " + result);
    return result;  // result !== ("Returning " + result)
}
// addTransparent(3,4);


//-----------------------------------------------------------//
// Currying:
// Currying is a technique for function decomposition:
function sum3(a) {
    return (b) => {
        return (c) => {
            return a + b + c;
        }
    }
}
// console.log(sum3(5)(6)(8));  // 19
// Usage:
// => Template functions
// => Code reuse
// => Partial implementation
// => Retain scope

//-----------------------------------------------------------//
// Converting a function with a given number of arguments into a function with smaller number of arguments
// Pass the remaining parameters when a result is needed
// The partially applied function can be used multiple times
// f(x, y) = x + y  <<<==>>>  g(x) = f(1, x)
// Currying always produces nested unary functions
// Partial application produces functions of arbitrary numberof arguments
// Currying is NOT partial application
// It can be	 implemented using partial application

//-----------------------------------------------------------//
// IFFE - Immediately- Invoked Function Expressions:
// - Define anonymous function expression
// - Invoke it immediately after declaration

// (function () {
//     let hello = 'Hello!';
//     // Variable hello is not accessible from the outside scope
//     console.log(hello);
// })();
//
// let result = (function () {
//     let name = 'Simeon';
//     console.log(name);
// })();

//-----------------------------------------------------------//
// Closure: ;-(
// One of the most important features of JS
// The scope of an inner function includes the scope of un outer function
// An inner function retains variables being used from the outer function scope
// even after the parent function has returned.

// Function returning Functions:
// A state is preserved in the outre function (CLOSURE):


