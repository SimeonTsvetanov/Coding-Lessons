function validate() {
    const emailInput = document.getElementById('email');  // GEt the input field

    // Set the Listener
    emailInput.addEventListener('change', (e) => {
        // Get the input Value:
        const value = emailInput.value;
        
        // Now check it with the regex:
        if (value.match(/^[a-z-\.]+@[a-z-\.]+\.[a-z]{2,4}/)) {
            // If we have a valid mail remove the class error:
            emailInput.classList.remove('error');
        } else {
            // if we don't add the class error:
            emailInput.classList.add('error');
        }
    });
}
