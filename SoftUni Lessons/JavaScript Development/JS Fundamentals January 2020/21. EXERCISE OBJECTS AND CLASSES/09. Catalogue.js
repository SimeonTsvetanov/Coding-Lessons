function catalogue(input) {
    // Mask
    let letters = [];  // We keep all the letters - objects: here

    class Letter {
        constructor(letter) {
            this.name = letter;  // Example: A, B, C, D
            this.products = [];  // Each letter will have it's own storage
        }
    }

    class Product{
        constructor(name, price) {
            this.name = name;  // Example: Cola
            this.price = price;  // Example: 2.50
        }
    }

    for (let line of input) {
        let name = line.split(' : ')[0];  // Product name
        let price = Number(line.split(' : ')[1]);  // Product price
        let product = new Product(name, price);  // Create the product object.
        let checkLetter = name[0];  // The letter we need to check

        // now lets see if we have that letter in the storage
        let present = false;
        for (let currentLetter of letters) {
            if (currentLetter.name === checkLetter) {
                // We have this letter already.
                present = true;
                currentLetter.products.push(product);  // We add the product to the letter storage.
                break;  // Get out of the loop.
            }
        }
        if (!present) {  // If, we don't have the letter
            // We have to add new Letter:
            let newLetter = new Letter(checkLetter);  // Create the letter object
            newLetter.products.push(product);  // Add the product to the letter storage
            letters.push(newLetter);  // Add the letter to the main storage
        }
    }

    // Sort the letters alphabetically.
    letters.sort((letterA, letterB) => letterA.name.localeCompare(letterB.name));

    // And let's print the result:
    for (let letter of letters) {
        console.log(letter.name);  // Print the letter

        // Now lets sort the letter storage (products) alphabetically:
        letter.products.sort((productA, productB) => productA.name.localeCompare(productB.name));
        // And print the storage of products
        for (let product of letter.products) {
            console.log(`  ${product.name}: ${product.price}`);
        }
    }
}


catalogue([
    'Appricot : 20.4', 
    'Fridge : 1500', 
    'TV : 1499', 
    'Deodorant : 10', 
    'Boiler : 300', 
    'Apple : 1.25', 
    'Anti-Bug Spray : 15', 
    'T-Shirt : 10'
]);  
// Should return:
// A
//   Anti-Bug Spray: 15
//   Apple: 1.25
//   Appricot: 20.4
// B
//   Boiler: 300
// D
//   Deodorant: 10
// F
//   Fridge: 1500
// T
//   T-Shirt: 10
//   TV: 1499

 

