// shortlink: https://git.io/JfhLj


class ChristmasDinner {
    constructor(budget) {
        this.budget = budget;
        this.dishes = [];
        this.products = [];
        this.guests = {};  // <--- Make sure that this s**t is an Object!
    }

    get budget() {
        return this._budget;
    }

    set budget(value) {
        if (Number(value) >= 0) { this._budget = value; }
        else { throw new Error("The budget cannot be a negative number"); }
    }

    shopping(array) {
        let product = array[0]; let price = Number(array[1]);
        if (this.budget - price < 0) { throw new Error(`Not enough money to buy this product`); }
        this.products.push(product);
        this.budget -= price;
        return `You have successfully bought ${product}!`;
    }

    recipes(recipe) {
        recipe.productsList.map(product => {
            if (!this.products.includes(product)) { throw new Error("We do not have this product"); }
        });
        this.dishes.push(recipe);
        return `${recipe.recipeName} has been successfully cooked!`
    }

    inviteGuests(nameToFind, dishToFind) {
        let dish = this.dishes.find(x => x.recipeName === dishToFind);
        if (!dish) { throw new Error(`We do not have this dish`); }
        if (this.guests.hasOwnProperty(nameToFind)) { throw new Error(`This guest has already been invited`); }
        this.guests[nameToFind] = dishToFind;
        return `You have successfully invited ${nameToFind}!`
    }

    showAttendance() {
        let result = '';
        for (let [name, dish] of Object.entries(this.guests)) {
            let products = this.dishes.find(recipe => recipe.recipeName === dish).productsList.join(', ');
            result += `${name} will eat ${dish}, which consists of ${products}\n`;
        }
        return result.trim();
    }
}

let dinner = new ChristmasDinner(300);

dinner.shopping(['Salt', 1]);
dinner.shopping(['Beans', 3]);
dinner.shopping(['Cabbage', 4]);
dinner.shopping(['Rice', 2]);
dinner.shopping(['Savory', 1]);
dinner.shopping(['Peppers', 1]);
dinner.shopping(['Fruits', 40]);
dinner.shopping(['Honey', 10]);

dinner.recipes({
    recipeName: 'Oshav',
    productsList: ['Fruits', 'Honey']
});
dinner.recipes({
    recipeName: 'Folded cabbage leaves filled with rice',
    productsList: ['Cabbage', 'Rice', 'Salt', 'Savory']
});
dinner.recipes({
    recipeName: 'Peppers filled with beans',
    productsList: ['Beans', 'Peppers', 'Salt']
});
dinner.inviteGuests('Ivan', 'Oshav');
dinner.inviteGuests('Petar', 'Folded cabbage leaves filled with rice');
dinner.inviteGuests('Georgi', 'Peppers filled with beans');

console.log(dinner.showAttendance());

// Should Return:
// Ivan will eat Oshav, which consists of Fruits, Honey
// Petar will eat Folded cabbage leaves filled with rice, which consists of Cabbage, Rice, Salt, Savory
// Georgi will eat Peppers filled with beans, which consists of Beans, Peppers, Salt
