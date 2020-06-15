function breakfastRobot() {
    const microElements = {
        protein: 0,
        carbohydrate: 0,
        fat: 0,
        flavour: 0
    };

    const recipes = {
        apple: {carbohydrate: 1, flavour: 2, order: ['carbohydrate', 'flavour']},
        lemonade: {carbohydrate: 10, flavour: 20, order: ['carbohydrate', 'flavour']},
        burger: {carbohydrate: 5, fat: 7, flavour: 3, order: ['carbohydrate', 'fat', 'flavour']},
        eggs: {protein: 5, fat: 1, flavour: 1, order: ['protein', 'fat', 'flavour']},
        turkey: {protein: 10, carbohydrate: 10, fat: 10, flavour: 10, order: ['protein', 'carbohydrate', 'fat', 'flavour']},
    };

    const operations = {
        restock,
        prepare,
        report,
    };

    function restock(element, quantity) {
        microElements[element] += quantity;
        return 'Success';
    }

    function prepare(recipe, quantity) {
        const required = Object.assign({}, recipes[recipe]);
        required.order.map(key => required[key] *= quantity);
        for (let element of required.order) {
            if (microElements[element] < required[element]) {
                return `Error: not enough ${element} in stock`;
            }
        }
        required.order.map(key => microElements[key] -= required[key]);
        return 'Success';
    }

    function report() {
        return `protein=${microElements.protein} carbohydrate=${microElements.carbohydrate} fat=${microElements.fat} flavour=${microElements.flavour}`;
    }

    function manager(command) {
        const tokens = command.split(' ');
        return operations[tokens[0]](tokens[1], Number(tokens[2]));
    }

    return manager;
}

let manager = breakfastRobot();
console.log(manager("restock flavour 50"));  // Success
console.log(manager("prepare lemonade 4"));  // Error: not enough carbohydrate in stock
