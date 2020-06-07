function solve() {
    // get the number input field Section:
    let numberInputField = document.querySelector('#input');
    // get the TO menu select area:
    let selectTo = document.querySelector('#selectMenuTo');
    // Get the Convert it Button:
    let button = document.querySelector('button');
    // Get the result Output Area:
    let resultingField = document.querySelector('#result');
    // resultingField.removeAttribute('disabled');
    // resultingField.removeAttribute('readonly');
    
    // Create the Options:
    let binary = document.createElement('option')
    binary.value = 'binary';
    binary.innerText = 'Binary';
    let hexadecimal = document.createElement('option')
    hexadecimal.value = 'hexadecimal';
    hexadecimal.innerText = 'Hexadecimal';
    // Add the options to the select menu:
    selectTo.appendChild(binary);
    selectTo.appendChild(hexadecimal);

    // Get that button listener in place:
    button.addEventListener('click', function () {
        let number = Number(numberInputField.value);
        let to = selectTo.options[selectTo.selectedIndex].text;
        
        // If we have input in the fields:
        if (number && to) {
            let result = ''

            switch (to) {
                case 'Binary':
                    result = (number >>> 0).toString(2);
                    break;
            
                case 'Hexadecimal':
                    console.log('hex')
                    result = number.toString(16).toUpperCase();
                    break;
            }
            resultingField.value = result;
        }
    })
}