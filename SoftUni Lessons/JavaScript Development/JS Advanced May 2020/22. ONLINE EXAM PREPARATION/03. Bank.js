class Bank {
    constructor(bankName) {
        this._bankName = bankName;
        this.allCustomers = [];
    }

    newCustomer(customer) {
        // The customer is of type object {firstName, lastName, personalId}.
        // Check if the customer is already a customer of the bank. If so you should throw an Error:
        this.allCustomers.map(oldCustomer => {
            if (oldCustomer.personalId === customer.personalId) {
                throw new Error(`${oldCustomer.firstName} ${oldCustomer.lastName} is already our customer!`);
            }
        });

        // Otherwise this function should add the customer as new one and return the customer details.
        let newClient = {
            firstName: customer.firstName,
            lastName: customer.lastName,
            personalId: Number(customer.personalId),
            totalMoney: 0,
            transactions: [],
        };
        this.allCustomers.push(newClient);
        return customer;
    }

    depositMoney (personalId, amount) {
        // If we have the person add the amount to the corresponding customer
        // in a property named totalMoney and store the transaction information to this customer

        let result = '';
        this.allCustomers.map(customer => {
            if (customer.personalId === Number(personalId)) {
                customer.totalMoney += amount;
                // NoOne expected to have that transactions shit...
                customer.transactions.push(`${customer.firstName} ${customer.lastName} made deposit of ${amount}$!`);
                // Set the result
                result = `${customer.totalMoney}$`;
            }
        });

        // Check if the given personalId corresponds to a customer in the customers array, if not throw a new error:
        // Or if we have the result, then: return the total money of the corresponding customer and a dollar sign:
        if (result) { return result; }
        else { throw new Error(`We have no customer with this ID!`); }
    }

    withdrawMoney (personalId, amount) {
        // Both the personalId and the amount are numbers.
        let result = '';
        this.allCustomers.map(customer => {
            if (customer.personalId === personalId) {
                // If there is a customer with the given personalId,
                // check if the customer has enough money in his account, to withdraw the given amount.
                // If the money is not enough throw a new error:
                if (amount > customer.totalMoney) {
                    throw new Error(`${customer.firstName} ${customer.lastName} does not have enough money to withdraw that amount!`);
                }
                // Otherwise subtract the amount from the totalMoney  of the customer
                // and store the transaction information to this customer,
                // then return the total money of the corresponding customer and a dollar sign:
                // “{totalMoney}$”
                customer.totalMoney -= amount;
                // This transactions shit is ugly...
                customer.transactions.push(`${customer.firstName} ${customer.lastName} withdrew ${amount}$!`);
                result = `${customer.totalMoney}$`;
            }
        });

        // If the result is a string then return it:
        if (result) { return result; }
        // Check if the given personalId corresponds to a customer in the customers array, if not throw a new error:
        else { throw new Error(`We have no customer with this ID!`); }
    }

    customerInfo (personalId) {
        // The personalId is of type number.
        let result = '';
        this.allCustomers.map(customer => {
            if (customer.personalId === personalId) {
                result = `Bank name: ${this._bankName}\nCustomer name: ${customer.firstName} ${customer.lastName}\nCustomer ID: ${customer.personalId}\nTotal Money: ${customer.totalMoney}$`;
                if (customer.transactions.length > 0) {
                    result += '\nTransactions:';
                    for (let count = customer.transactions.length; count > 0; count -= 1) {
                        result += `\n${count}. ${customer.transactions[count - 1]}`;
                    }
                }
            }
        });

        // return the whole information
        if (result) { return result; }
        // If we don't have an result: throw a new error:
        else { throw new Error(`We have no customer with this ID!`); }
    }
}