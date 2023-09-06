function mask (params) {
    let month = params
    // MASK
    let months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ];
    (month >= 1 && month <= 12) ? console.log(months[month - 1]) : console.log('Error!');
}

mask(2);
// February

mask(13);
// Error!
