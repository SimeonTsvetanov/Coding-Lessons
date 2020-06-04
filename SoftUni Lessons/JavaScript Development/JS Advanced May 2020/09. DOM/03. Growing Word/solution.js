function growingWord() {
    // Get the paragraph:
    let paragraph = document.querySelector('#exercise > p');
    
    // Set the DELTA Changes of the color using an object
    let change = { 'blue': 'green', 'green': 'red', 'red': 'blue' };

    // We need to check if we have the attribute style first:
    if (!paragraph.hasAttribute('style')) {
        // If we don't we need to apply the 2 px size and blue color
        paragraph.setAttribute('style', 'color:blue; font-size: 2px');
    } else {
        // Or if we do we need to change the fontsize *= 2 and swap the color
        // Set the new size and colors:
        let size = Number(paragraph.style.fontSize.split('').filter(Number).join('')) * 2;
        let color = change[paragraph.style.color];
        
        // Apply it to the paragraph.
        paragraph.setAttribute('style', `color:${color}; font-size: ${size}px`);
    }
}