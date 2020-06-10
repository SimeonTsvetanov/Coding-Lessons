function solve() {
    const inputText = document.getElementById('searchField');
    const table = document.querySelector('tbody');

    document.getElementById('searchBtn').addEventListener('click', function () {
        Array.from(table.rows).forEach(row => {
            console.log(row.textContent);
            if (row.textContent.toLowerCase().includes(inputText.value.toLowerCase())) {
                row.classList.add('select');
            } else {
                row.classList.remove('select');
            }
        });
        inputText.value = '';
    });
}
