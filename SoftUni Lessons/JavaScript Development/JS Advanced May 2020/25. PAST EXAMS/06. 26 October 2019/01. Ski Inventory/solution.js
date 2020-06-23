function solve() {
    //Todo... Not mine solution I'll make one later...
    function makeEl(type, text) {
        let el = document.createElement(type);
        el.textContent = text;
        return el;
    }

    const addBtn = document.querySelector('#add-new > button');
    let avlProd = document.getElementById('products').children[1].children;
    const products = document.getElementById('products').children[1];
    const myProducts = document.getElementById('myProducts').children[1];
    let totalPriceHTML = document.getElementsByTagName('h1')[1];
    let totalPrice = 0;

    addBtn.addEventListener('click', function () {
        function priceSec() {
            let div = document.createElement('div');
            div.appendChild(makeEl('strong', Number(price).toFixed(2)));
            div.appendChild(makeEl('button', `Add to Client's List`));
            return div;
        }
        function makeProduct() {
            let li = document.createElement('li');
            li.appendChild(makeEl('span', name));
            li.appendChild(makeEl('strong', `Available: ${Number(qty).toFixed()}`));
            li.appendChild(priceSec());
            return li;
        }
        const name = document.getElementById('add-new').children[1].value;
        const qty = document.getElementById('add-new').children[2].value;
        const price = document.getElementById('add-new').children[3].value;

        products.appendChild(makeProduct());

        Array.from(avlProd).forEach(function (e) {
            let eBtn = e.lastElementChild.lastElementChild;
            eBtn.addEventListener('click', function (e) {
                e.preventDefault();
                const button = e.target;
                let myItmName = button.parentNode.previousSibling.previousSibling;
                let myItemValue = Number(button.previousSibling.textContent);
                let itemQty = Number(button.parentNode.previousSibling.textContent.split(' ')[1]) - 1;
                if (itemQty < 1) {
                    products.removeChild(button.parentNode.parentNode);
                } else {
                    button.parentNode.previousSibling.textContent = `Available: ${itemQty.toFixed()}`;
                }

                let myItem = makeEl('li', myItmName.textContent)
                myItem.appendChild(makeEl('strong', myItemValue.toFixed(2)));
                myProducts.appendChild(myItem);

                totalPrice += myItemValue;
                totalPriceHTML.textContent = `Total Price: ${totalPrice.toFixed(2)}`;
            });
        });
    });

    const filterBtn = document.querySelector('#products > div > button');
    filterBtn.addEventListener('click', function () {
        let filterWord = document.getElementById('filter').value.toLowerCase();
        Array.from(avlProd).map(p => {
            let name = p.firstElementChild.textContent.toLowerCase();
            p.style.display = name.includes(filterWord) ? 'block' : 'none';
        });
    });

    const buyBtn = document.querySelector('#myProducts > button');
    buyBtn.addEventListener('click', function () {
        totalPrice = 0;
        totalPriceHTML.textContent = `Total Price: ${totalPrice.toFixed(2)}`;
        myProducts.innerHTML = '';
    });
}