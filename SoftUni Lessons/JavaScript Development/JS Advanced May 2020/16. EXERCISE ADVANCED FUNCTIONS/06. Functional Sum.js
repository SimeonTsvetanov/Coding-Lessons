function add(x) {
    function sum(a) {
        x += a;
        return sum;
    }
    sum.toString = () => x;
    return sum;
}

console.log(add(1)(3)(2)); // Should Return: 6
