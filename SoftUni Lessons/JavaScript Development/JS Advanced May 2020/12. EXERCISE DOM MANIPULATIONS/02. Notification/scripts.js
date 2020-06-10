function notify(message) {
    let notification = document.getElementById("notification");  // Get the Notification div
    notification.innerHTML = message;                            // Add the message to it
    notification.style.display = 'block';                        // Change the display style to block
    setTimeout(function () {                                     // Turn on the 2 seconds function
        notification.style.display = 'none';                     // When it end to hide the notification
    }, 2000);   
}