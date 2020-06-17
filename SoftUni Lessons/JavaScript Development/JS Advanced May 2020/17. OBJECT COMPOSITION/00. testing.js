/*
What is OC?
    -Combining simple objects or data types into more complex ones.

let student = {
    firstName: 'Simeon',
    lastName: 'Tsvetanov',
    age: 30,
    location: { lat: 42.698, lng: 23.322 },
};

console.log(student);
console.log(student.location.lat);
 */

// Composing Objects:
// let name = 'Smolyan';
// let population = 33000;
// let country = 'Bulgaria';
// let town = { name, population, country };
// console.log(town);
// town.location = { lat: 42.698, lng: 23.322 };
// console.log(town);

// Combining Data with Functions:
// let rect = {
//     width: 10,
//     height: 4,
//     grow: function (w, h) {
//         this.width += w; this.height += h;
//     },
//     print: function () {
//         console.log(`[${this.width} x ${this.height}]`);
//     },
// };
// rect.print();
// rect.grow(2, 3);
// rect.print();

// Printing Objects ToString() Function:
// let rect = {
//     width: 10,
//     height: 4,
//     toString: function () {
//         return `rect[${this.width} x ${this.height}]`;
//     },
// };
// console.log('' + rect);

// Destructuring:
// the ability to dive into an array or object and reference something inside of it more directly.
// const department = {
//     name: 'Engineering',
//     data: {},
// };
// const { data } = department;  // Now data references the data object directly,
// const objectList = [ { key: 'value' }, { key: 'value' }, { key: 'value' } ];
// const [ obj, obj1, obj2 ] = objectList;
// // now each object can be referenced directly
// console.log(department);
// console.log(data);

// const department = {
//     name: "Engineering",
//     data: {
//         director: {
//             name: 'John',
//             position: 'Engineering Director'
//         },
//         employees: [],
//         company: 'Quick Build'
//     }
// };
// const {data: {director}} = department;
// director is { name: 'John', position: 'Engineering Director'}

// Nested Destructing:
// const department = {
//     name: "Engineering",
//     data: {
//         director: {
//             name: 'John',
//             position: 'Engineering Director'
//         },
//         employees: [],
//         company: 'Quick Build'
//     }
// };
// const {data: {director}} = department;
// director is { name: 'John', position: 'Engineering Director'}


/*
Destructuring Nested Arrays
You need to know the position of what you're looking for
Provide a reference variable (or comma placeholder)
for each element up and until the one you're looking for
 */

// const departments = [
//     [
//         'Engineering', 
//         [
//             'secretary',
//              'director',
//              'worker'
//         ]
//     ], 
//     [
//         'Accounting', 
//         [
//             'director',
//             'accountant'
//         ]
//     ]
//     ];
// const [[name, positions]] = departments;
// console.log(name, positions);
// name is 'Engineering'
// positions is [ 'secretary', 'director', 'worker' ]


// Objects and Arrays Destructuring:
// const employees = [
//     { name: 'Simeon', 'position': 'man'},
//     { name: 'Iliyana', position: 'woman'},
// ];
// const [ {name} ] = employees;
// console.log(name); // Simeon
// const company = {
//     employees: ['John', 'Jane', 'Sam', 'Suzanne'],
//     name: 'Quick Build',
// };
// const {employees:[employee]} = company; // employee is 'John'
// console.log(employee);


// Forms of Object Composition
/*
Aggregation:
    - Object is formed from an enumerable collection of sub-objects
    - An aggregate is an object which contains other objects
    - When to use:
    - Collections of objects which need to share common operations
    - When you want a single item to share the same interface as many items

Concatenation:
    - Concatenation is when an object is formed by adding new properties to an existing object
    - When to use:
        - merging JSON objects
        - Creating updates to immutable state
        - Etc…
 */

// Concatenation Example:
// const objs = [
//     {name: 'Peter',age:35 },
//     {age: 22},
//     {name: "Steven"},
//     {height:180}
// ];
// console.log(objs);
// const concatenate = (a, o) => ({...a, ...o});
// const c = objs.reduce(concatenate, {});
// console.log(c);// { name: 'Steven', age: 22, height: 180 }

/*
Delegation:
    - Delegation is commonly used to imitate class inheritance in JavaScript
    - Composes objects by linking together an object delegation chain:
        - An object forwards property lookups to another object
        - [].map() delegates to Array.prototype.map()
 */
// const objs = [
//     {name: 'Peter',age:35},
//     {age: 22},
//     {name: "Steven"},
//     {height:180}
// ];
// const delegate = (a, b) => Object.assign(Object.create(a), b);
// const d = objs.reduceRight(delegate, {});
// console.log(d); // { name: 'Peter', age: 35 }
// console.log(d.height); // 180

// Summary
/*
Object composition combines data and functions into JS objects
Three main types of object composition
Aggregation - forming an object from an enumerable  collection
Concatenation - adding new properties
Delegation - imitates class inheritance
 */

let foo = { a: [1, 2, 3], b: 2};
let bar = { a: 2, c: 'str'};
let mar = {...foo, ...bar};
foo.b = 3;
console.log(mar);