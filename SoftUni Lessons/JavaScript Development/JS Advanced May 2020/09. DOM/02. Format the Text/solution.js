function solve() {
    // Get the Text
    let array = document
        .querySelector('#input')  // By id 'input'
        .innerText.split('. ')  // And Split in on '. ' as an Array
        .filter(x => x.length >= 1); // And ilter the emptyones.

    // Get the output DIV
    let div = document.getElementById('output')

    // Now let's iterate trough the array by each 3 elements:
    for (let index = 0; index < array.length; index += 3) {
        // Create new array from the 3 elements:
        let text = [array[index], array[index + 1], array[index + 2]]
        .filter(Boolean)  // Remove the empty slots
        .join('. ');  // Create a String Joined by '. '
        
        // Create new p element with and append the text to it:
        let p = document.createElement('p');
        p.innerText = text;
        
        // FINALLY - append the p to the Output div:
        div.appendChild(p);
    }
}
