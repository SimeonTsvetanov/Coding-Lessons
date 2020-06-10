function solve() {
    // Get the input input text area:
    let inputArea = document.querySelectorAll('textarea')[0];
    // Get the Generate Button:
    let generateButton = document.querySelectorAll('button')[0];
    // Get the tableBody where we will append the new products:
    let tBody = document.querySelector('tbody');
    // Get the buy Output Area:
    let outputArea = document.querySelectorAll('textarea')[1];
    // Get the Buy Button:
    let buyButton = document.querySelectorAll('button')[1];
    
    // Set the event listener for the the JSON file:
    generateButton.addEventListener('click', function (e) {
        // Stop if no input:
        if (!inputArea.value) { return; }

        // Get the JSON And iterate the objects in it:
        let json = JSON.parse(inputArea.value);
        json.map(product => {
            // Create the new tr for the new product:
            let newProduct = document.createElement('tr');

            // Get/Append the Image:
            let img = document.createElement('img');
            img.src = product.img
            let imgTd = document.createElement('td');
            imgTd.appendChild(img);
            newProduct.appendChild(imgTd);
            
            // Get/Append the Name
            let nameTd = document.createElement('td');
            let nameP = document.createElement('p');
            nameP.textContent = product.name;
            nameTd.appendChild(nameP);
            newProduct.appendChild(nameTd);

            // Get/Append the Price
            let priceTd = document.createElement('td');
            let priceP = document.createElement('p');
            priceP.textContent = product.price;
            priceTd.appendChild(priceP);
            newProduct.appendChild(priceTd);

            // Get/Append the Decoration factor 
            let decFactorTd = document.createElement('td');
            let decFactorP = document.createElement('p');
            decFactorP.textContent = product.decFactor;
            decFactorTd.appendChild(decFactorP);
            newProduct.appendChild(decFactorTd);

            // Create/Append the input type:
            let checkedTd = document.createElement('td');
            checkedTd.innerHTML = '<input type="checkbox"/>';
            newProduct.appendChild(checkedTd);
            
            // Append the new Product in the tbody:
            tBody.appendChild(newProduct);
        });
    });

    // Set the function for when the Buy button is clicked 
    buyButton.addEventListener('click', function (e) {
        let boughtFurniture = [];
        let totalPrice = 0;
        let totalDecorationFactor = 0;
        

        // Iterate the products and check if they are selected:
        for (let kid = 1; kid < tBody.children.length; kid++) {
            if (tBody.children[kid].children[4].children[0].checked === true) {
                // If selected:
                let name = tBody.children[kid].children[1].firstChild.textContent;
                let price = Number(tBody.children[kid].children[2].firstChild.textContent);
                let decFactor = Number(tBody.children[kid].children[3].firstChild.textContent);
                boughtFurniture.push(name);
                totalPrice += price;
                totalDecorationFactor += decFactor;
            }
        }
        // Get the average Decoration factor:
        let averageDecorationFactor = totalDecorationFactor / boughtFurniture.length;

        // Create the resulting Text:
        let result = "Bought furniture: " + boughtFurniture.join(', ');
        result += `\nTotal price: ${totalPrice.toFixed(2)}`;
        result += `\nAverage decoration factor: ${averageDecorationFactor}`
        
        // Append the resulting Text to the output area:
        outputArea.textContent = result;
    });
}


let testJson = [
    {
        "img":"https://www.ikea.com/PIAimages/0447583_PE597395_S5.JPG",
        "name": "Sofa",
        "price": "259",
        "decFactor":"0.4"

    },
    {
        "img":"https://cdn.jysk.ca/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/7/0/7011671065_3dr_sonoma.jpg",
        "name": "Wardrobe",
        "price": "120",
        "decFactor":"1.2"
    }
]