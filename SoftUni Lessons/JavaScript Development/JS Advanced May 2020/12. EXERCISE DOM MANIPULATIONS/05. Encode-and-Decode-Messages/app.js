function encodeAndDecodeMessages() {
    // First Get the Elements we need:
    let encodeArea = document.querySelectorAll('textarea')[0];    
    let encodeButton = document.querySelectorAll('button')[0];    
    let decodeArea = document.querySelectorAll('textarea')[1];
    let decodeButton = document.querySelectorAll('button')[1];

    // Set the Listener for the Encode And Send it:
    encodeButton.addEventListener('click', function (e) {
        // Get the text:
        let text = encodeArea.value;
        // Stop it, if there is no text;
        if (!text) { return; }
        // Now we need to encode it:
        let encodedMessage = encoder(text); 
        // Add it to the decode Area:
        decodeArea.innerText = encodedMessage;
        // Clear the encode text area:
        encodeArea.value = ''
    });

    // Set the Listener for the Decode Event:
    decodeButton.addEventListener('click', function(e) {
        // Get the decoded:
        let decoded = decodeArea.value;
        // Now lets get it decoded:
        let text = decoder(decoded);
        // And Change the Decoded Area with the NOW decoded text:
        decodeArea.value = text; 
    });

    function encoder(text) {
        // it will return the given text encoded:
        // Each letter in ascii - 1
        let encoded = '';
        text.split('').map(letter => {
            encoded += String.fromCharCode(letter.charCodeAt(0) + 1);
        })
        return encoded;
    }

    function decoder(decoded) {
        // It will return the given encoded text decoded:
        // Each letter in ascii + 1
        let text = '';
        decoded.split('').map(letter => {
            text += String.fromCharCode(letter.charCodeAt(0) - 1);
        })
        return text;
    }
}