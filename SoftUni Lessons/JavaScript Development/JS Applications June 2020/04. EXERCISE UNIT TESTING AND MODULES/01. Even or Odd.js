// To test the code go in /tests and run the corresponding file name :)

function isOddOrEven(string) {
    if (typeof(string) !== 'string') {
        return undefined;
    }
    if (string.length % 2 === 0) {
        return "even";
    }

    return "odd";
}

module.exports = { isOddOrEven };
