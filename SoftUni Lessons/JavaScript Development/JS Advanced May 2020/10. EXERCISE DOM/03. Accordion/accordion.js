function toggle() {
    let button = document.querySelector('.button');  // Get the Button
    let extra = document.querySelector('#extra');  // Get the Extra section
    
    // Now lets swap them out ;D
    if (button.textContent === 'More') {
        button.textContent = 'Less';
        extra.style.display = 'block';  // Show
    } else {
        button.textContent = 'More';
        extra.style.display = 'none';  // Hide
    }
}
