function cookingByNumbers(input) {
    // Mask
    let num = Number(input.shift());

    for (const command of input) {
        switch (command) {
            case 'chop':
                num /= 2;
                break;
            case 'dice':
                num = Math.sqrt(num);
                break;
            case 'spice':
                num += 1;
                break;
            case 'bake':
                num *= 3;
                break;
            case 'fillet':
                num *= 0.8;
                break;
        }
        console.log(num);
    }
}

cookingByNumbers(['32', 'chop', 'chop', 'chop', 'chop', 'chop']);  // Should return:
// 16
// 8
// 4
// 2
// 1

cookingByNumbers(['9', 'dice', 'spice', 'chop', 'bake', 'fillet']);  // Should return:
// 3
// 4
// 2
// 6
// 4.8
