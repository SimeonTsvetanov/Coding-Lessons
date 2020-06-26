// Short link: https://git.io/JfjFL

function solve() {
    // Available Products:
    let availableProductS = document.querySelector('#products');
    let availableProductSUL = document.querySelector('#products > ul');
    let availableProductSFilterInputField = document.querySelector('#filter');
    let availableProductFilterBtn = document.querySelector('.filter > button');
    availableProductFilterBtn.addEventListener('click', filterUL);

    // Add Products:
    let addProductS = document.querySelector('#add-new');
    let addNameField = addProductS.querySelectorAll('input').item(0);
    let addQuantityField = addProductS.querySelectorAll('input').item(1);
    let addPriceField = addProductS.querySelectorAll('input').item(2);
    let addButton = addProductS.querySelector('button');
    addButton.addEventListener('click', addItem);

    // Total Price:
    let totalPriceH1 = document.querySelectorAll('h1').item(1);

    // My Products:
    let myProductsS = document.querySelector('#myProducts');
    let myProductsSUL = document.querySelector('#myProducts > ul');
    let myProductsSBtn = document.querySelector('#myProducts > button');
    myProductsSBtn.addEventListener('click', buyAll);

    function addItem(e) {
        e.preventDefault();
        let name = addNameField.value; let quantity = addQuantityField.value; let price = Number(addPriceField.value);
        if (!(name && quantity && price)) { return; }

        // Create the product
        let product = document.createElement('li');
        product.innerHTML = `<span>${name}</span><strong>Available: ${quantity}</strong><div><strong>${price.toFixed(2)}</strong><button>Add to Client's List</button></div>`
        // Set the Event Listener:
        product.addEventListener('click', clickedOnProduct);

        // Append the product
        availableProductSUL.appendChild(product);

        // Clean the form
        addNameField.value = ''; addQuantityField.value = ''; addPriceField.value = '';
    }

    function clickedOnProduct(e) {
        if (!(e.target.textContent === `Add to Client's List`)) { return; }
        let product = e.target.parentElement.parentElement;
        let name = product.firstElementChild.textContent;

        let availableField = product.querySelectorAll('strong').item(0);
        let available = Number(availableField.textContent.split(' ')[1]);

        let price =  Number(product.querySelectorAll('strong').item(1).textContent);
        let current = Number(totalPriceH1.textContent.split(' ')[2]);
        let total = price + current;
        totalPriceH1.textContent = `Total Price: ${total.toFixed(2)}`;

        let boughtProduct = document.createElement('li');
        boughtProduct.innerHTML = `${name}<strong>${price.toFixed(2)}</strong>`;
        myProductsSUL.appendChild(boughtProduct);

        available -= 1;
        if (available === 0) {
            product.parentElement.removeChild(product);
        } else {
            availableField.textContent = `Available: ${available}`;
        }
    }

    function filterUL(e) {
        let criteria = availableProductSFilterInputField.value;
        if (!criteria) { return; }

        let items = Array.from(availableProductSUL.querySelectorAll('li'));
        availableProductSUL.innerHTML = '';
        items.forEach(item => {
            if (!(item.firstElementChild.textContent.includes(criteria))) {
                item.style.display = 'none';
            }
            availableProductSUL.appendChild(item);
        })
    }

    function buyAll(e) {
        myProductsSUL.innerHTML = '';
        totalPriceH1.textContent = `Total Price: 0.00`;
    }
}
