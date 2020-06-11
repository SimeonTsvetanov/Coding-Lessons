function solve() {
    // This task is SOOOO stupid..... 
    // There is no mention of black background or white color in the description.
    // WTF

    // get the button:
    let container = document.querySelector('#container');
    let btn = document.querySelector('#dropdown');
    let box = document.querySelector('#box');
    let firstColor = box.style.backgroundColor;
    let colorsList = document.querySelector('#dropdown-ul');

    const ddList = document.querySelector('#dropdown-ul');
    ddList.style.display = '';

    btn.addEventListener('click', function (e) {
        if (ddList.style.display == '' || ddList.style.display == 'none') {
            // So its closed
            ddList.style.display = 'block';
            colorsList.addEventListener('click', function (e) {
                box.style.backgroundColor = e.target.textContent;
                box.style.color = 'black';
            });
        } else {
            // It is open 
            box.style.backgroundColor = 'black';
            box.style.color = 'white';
            ddList.style.display = 'none';
        }
    });
}