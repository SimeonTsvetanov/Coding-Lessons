function solve() {
    let addButton = document.querySelector('form').lastElementChild;
    addButton.addEventListener('click', addBook);

    let newBooks = document.querySelectorAll('.bookShelf')[1];
    let oldBooks = document.querySelectorAll('.bookShelf')[0];

    function addBook(e) {
        e.preventDefault();
        let [titleField, yearField, priceField] = document.querySelectorAll(`form > input`);
        let title = titleField.value; let year = yearField.value; let price = Number(priceField.value);

        if ((!(title)) || (price < 0) || (year < 0)) { return; }
        year < 2000 ? price *= 0.85 : 'pass';

        let book = document.createElement('div');
        book.classList.add('book');

        let p = document.createElement('p');
        p.textContent = `${title} [${year}]`;
        book.appendChild(p);

        let buttonPrice = document.createElement('button');
        buttonPrice.textContent = `Buy it only for ${price.toFixed(2)} BGN`;
        buttonPrice.addEventListener('click', buy);
        book.appendChild(buttonPrice);

        if (year >= 2000) {
            let buttonOld = document.createElement('button');
            buttonOld.textContent = `Move to old section`;
            buttonOld.addEventListener('click', moveToOld);
            book.appendChild(buttonOld);

            newBooks.appendChild(book);
        } else {
            oldBooks.appendChild(book);
        }
        titleField.value = ''; yearField.value = ''; priceField.value = '';
    }

    function buy(e) {
        let book = e.target.parentElement;
        let parent = book.parentElement;
        parent.removeChild(book);
        let price = Number(book.children[1].textContent.split(' ')[4]);
        let profitMessage = document.querySelectorAll('h1')[1];
        let total = Number(profitMessage.textContent.split(' ')[3]) + price;
        profitMessage.textContent = `Total Store Profit: ${total.toFixed(2)} BGN`;
    }

    function moveToOld(e) {
        let book = e.target.parentElement;

        let parent = book.parentElement;
        parent.removeChild(book);

        let priceButton = book.children[1];
        let oldButton = book.children[2];
        let price = Number(book.children[1].textContent.split(' ')[4]) * 0.85;
        priceButton.textContent = `Buy it only for ${price.toFixed(2)} BGN`;
        book.removeChild(oldButton);

        oldBooks.appendChild(book);
    }
}