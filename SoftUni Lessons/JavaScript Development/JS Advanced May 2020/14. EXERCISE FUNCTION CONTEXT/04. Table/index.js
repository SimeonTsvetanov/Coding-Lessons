function solve() {
    // add event listener
    const tbody = document.querySelector('tbody');
    const items = tbody.querySelectorAll('tr')
    tbody.addEventListener('click', parseTable);

    function parseTable(e) {
        // find the selected element:
        const row = e.target.parentElement
        if (row.nodeName !== 'TR') { return; }
        
        if (row.style.backgroundColor !== '') {
            // if element has style -> remove it!
            row.style.backgroundColor = '';
        } else {
            // Else turn off all and light it.
            [...items].forEach(item => item.style.backgroundColor = '')
            row.style.backgroundColor = "#413f5e";
        }
    }
}
