function addItem() {
    // Get the Elements:
    let text = document.querySelector('#newItemText');
    let value = document.querySelector('#newItemValue');
    let select = document.querySelector('#menu')

    // Check if we have the input fields filled in:
    if (text.value && value.value) {
        // IF we DO:
        let option = document.createElement('option');  // Create the Option Element.
        option.setAttribute('value', value.value); // Set the option value.
        option.text = text.value;  // Set the actual text.
        select.appendChild(option);  // Append the option to the select menu.

        // And finally clear the input fields:
        text.value = '';
        value.value = '';
    }
}
