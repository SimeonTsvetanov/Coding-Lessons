class Storage {
    constructor(capacity) {
        this.capacity = capacity;
        this.storage = [];
    }

    get totalCost() {
        let total = 0;
        this.storage.forEach(x => {
            total += x.price * x.quantity;
        });
        return total;
    }

    addProduct(product) {
        if (this.capacity - product.quantity >= 0) {
            this.capacity -= product.quantity;
            this.storage.push(product);
        }
    }

    getProducts() {
        let result = [];
        this.storage.forEach(product => {
            result.push(JSON.stringify(product));
        });
        return result.join('\n');
    }
}
