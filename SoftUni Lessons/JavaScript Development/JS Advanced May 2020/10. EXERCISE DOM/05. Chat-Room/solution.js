function solve() {
    // First Let's grab the Input, Button and Chat Area:
    let button = document.querySelector("#send");
    let input = document.querySelector("#chat_input");
    let area = document.querySelector("#chat_messages");

    // Now lets pace the listener:
    button.addEventListener('click', function () {
        // If we don't have any value we won't continue:
        if (!input.value) { return; }

        // Lets Create the Message:
        let message = document.createElement('div');
        message.setAttribute("class", "message my-message");
        message.innerText = input.value;

        // And Append the message to the Chat Area:
        area.appendChild(message);

        // And clear the input field;
        input.value = '';
    });
}







