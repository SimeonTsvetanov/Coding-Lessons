function lockedProfile() {
    // Get the show more buttons in one place:
    let buttons = document.querySelectorAll('button');

    // Set the event listener for all the buttons in one loop:
    for (var i = 0; i < buttons.length; i++) {
		buttons[i].addEventListener("click", function(e) {
            // Find the hidden information DIV:
            hiddenInformationDiv = e.target.parentElement.children[9];
            
            // If the button is locked Don't do anything:
            if (e.target.parentElement.children[2].checked) {return;};
            
            // Now if the Menu is OPEN:
            actionButton = e.target.parentElement.children[10];
            
            if (actionButton.innerText === 'Show more') {
                // Change the button text
                actionButton.innerText = 'Hide it';
                // Change the hidden information to be shown:
                hiddenInformationDiv.style.display = 'block';
            } else {
                // Change the button text:
                actionButton.innerText = 'Show more'
                // Hide the information
                hiddenInformationDiv.style.display = 'none';
            }   
		});
    }
}