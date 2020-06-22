function solution() {
    let addButton = document.querySelectorAll('.card')[0].lastElementChild.lastElementChild;
    addButton.addEventListener('click', addGift);

    function addGift(e) {
        let nameField = e.target.parentElement.firstElementChild;  // Get the name field
        let name = nameField.value;  // get the new name
        if (!name) { return; }  // Don't continue if the name is empty

        let newGiftLi = createNewGift(name);  // Create the Gift
        appendGiftAndSortUl(newGiftLi);  // Append the gift + Sort the UL
        nameField.value = '';  // Clear the inputField;
    }

    function appendGiftAndSortUl(gift) {
        let listOfGiftsMenu = document.querySelectorAll('.card')[1];  // Get the menu
        let listOfGiftsUl = document.querySelectorAll('.card')[1].lastElementChild;  // Get the ul
        listOfGiftsUl.appendChild(gift);  // Append the gift
        listOfGiftsMenu.removeChild(listOfGiftsUl); // Remove the ul from the screen
        let sortedListOfGifts = sortListOfGifts(listOfGiftsUl); // Sort the Ul
        listOfGiftsMenu.appendChild(sortedListOfGifts); // Return the Ul on the screen
    }

    function sortListOfGifts(ul) {
        let items = [...ul.querySelectorAll('li')];
        ul.innerHTML = '';
        items.sort(((a, b) => a.textContent.localeCompare(b.textContent))).forEach(li => ul.appendChild(li));
        return ul;
    }

    function createNewGift(name) {
        let newGiftLi = document.createElement('li');
        newGiftLi.classList.add('gift');
        newGiftLi.textContent = name;
        let sendButton = document.createElement('button');
        sendButton.setAttribute('id', 'sendButton');
        sendButton.textContent = 'Send';
        sendButton.addEventListener('click', sendGift);
        newGiftLi.appendChild(sendButton);
        let discardButton = document.createElement('button');
        discardButton.setAttribute('id', 'discardButton');
        discardButton.textContent = 'Discard';
        discardButton.addEventListener('click', discardGift);
        newGiftLi.appendChild(discardButton);
        return newGiftLi;
    }

    function sendGift(e) {
        let sendGiftsUl = document.querySelectorAll('.card')[2].lastElementChild;  // Get the Send Gifts menu UL
        let giftToSend = e.target.parentElement; // Get the list item
        giftToSend.removeChild(giftToSend.lastElementChild); // Remove the buttons from the list item
        giftToSend.removeChild(giftToSend.lastElementChild); // Remove the buttons from the list item
        sendGiftsUl.appendChild(giftToSend); // Append the list item to the Send Gifts menu UL
    }

    function discardGift(e) {
        let discardedGiftsUl = document.querySelectorAll('.card')[3].lastElementChild;// Get the Discarded Gifts menu UL
        let giftToDiscard = e.target.parentElement; // Get the list item
        giftToDiscard.removeChild(giftToDiscard.lastElementChild); // Remove the buttons from the list item
        giftToDiscard.removeChild(giftToDiscard.lastElementChild); // Remove the buttons from the list item
        discardedGiftsUl.appendChild(giftToDiscard); // Append the list item to the Discarded Gifts menu UL
    }
}