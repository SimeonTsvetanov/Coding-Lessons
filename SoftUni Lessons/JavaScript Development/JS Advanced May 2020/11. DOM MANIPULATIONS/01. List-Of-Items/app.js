function addItem() {
    const newItem = document.querySelector('#newItemText'); // Get the text field value
    if (!newItem.value) { return; }                         // If it's Empty: Stop
    const list = document.querySelector('#items');          // Get the list Element
    const newItemList = document.createElement('li');       // Create the new list Element
    newItemList.innerText = newItem.value;                  // Add the text to the new element
    list.appendChild(newItemList)                           // Append the element to the list
    newItem.value = '';                                     // Clear the input field
}
 