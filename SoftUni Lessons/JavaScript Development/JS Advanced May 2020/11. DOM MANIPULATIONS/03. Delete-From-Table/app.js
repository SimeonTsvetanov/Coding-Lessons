function deleteByEmail() {
    // Done in Class:
    const emailTds = Array.from(document.querySelectorAll('#customers td:last-child'));
    console.log(emailTds);
    const emailInput = document.querySelector('input[name=email]');
    const resultDiv = document.querySelector('#result');
    
    resultDiv.innerText = '';

    const emailInputValue = emailInput.value;
    
    if (!emailInputValue) { return; }
    const td = emailTds.find(function (td) {return td.innerText === emailInputValue});
    if (!td) {resultDiv.innerText = 'Not found.'; return; }

    td.parentElement.remove();
    resultDiv.innerText = 'Deleted.';
}
