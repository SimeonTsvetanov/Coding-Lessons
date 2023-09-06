function mask (num) {
    // MASK
    if (num !== 100) {
        console.log(`${num}% [${'%'.repeat(num / 10)}${'.'.repeat(10 - (num / 10))}]`);
        console.log('Still loading...');
    } else {
        console.log('100% Complete!');
        console.log('[%%%%%%%%%%]')
    }
}

mask(30);
// 30% [%%%.......]
// Still loading...

console.log('-------------------------------------');

mask(50);
// 50% [%%%%%.....]
// Still loading...

console.log('-------------------------------------');

mask(100);
// 100% Complete!
// [%%%%%%%%%%]
