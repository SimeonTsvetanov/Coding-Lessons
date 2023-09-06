function mask (args) {
    // MASK ... i hate points!!!
    let [x1, y1, x2, y2] = args

    function getDistance(x1, y1, x2, y2) {
        let y = x2 - x1;
        let x = y2 - y1;

        return Math.sqrt(x * x + y * y);
    }

    let a = (Number.isInteger(getDistance(x1, y1, 0 , 0))) ? 'valid' : 'invalid';
    let b = (Number.isInteger(getDistance(x2, y2, 0 , 0))) ? 'valid': 'invalid';
    let c = (Number.isInteger(getDistance(x1, y1, x2, y2))) ? 'valid': 'invalid';

    console.log(`{${x1}, ${y1}} to {0, 0} is ${a}`);
    console.log(`{${x2}, ${y2}} to {0, 0} is ${b}`);
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${c}`);
}

mask([3, 0, 0, 4]);
// {3, 0} to {0, 0} is valid
// {0, 4} to {0, 0} is valid
// {3, 0} to {0, 4} is valid

console.log('-------------------------------------');

mask([2, 1, 1, 1]);
// {2, 1} to {0, 0} is invalid
// {1, 1} to {0, 0} is invalid
// {2, 1} to {1, 1} is valid
