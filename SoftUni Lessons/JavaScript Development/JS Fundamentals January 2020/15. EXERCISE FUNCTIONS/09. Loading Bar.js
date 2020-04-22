function loadingBar(percent) {
    // Mask
    let full = percent / 10;
    let empty = 10 - full;

    let bar = `[${'%'.repeat(full)}${'.'.repeat(empty)}]`;

    if (percent === 100) {
        console.log(`${percent} Complete!`);
        console.log(bar);
    } else {
        console.log(`${percent}% ${bar}`);
        console.log('Still loading...');
    }
}

loadingBar(30);  // Should return:
// 30% [%%%.......]
// Still loading...


loadingBar(50);  // Should return:
// 50% [%%%%%.....]
// Still loading...


loadingBar(100);  // Should return:
// 100% Complete!
// [%%%%%%%%%%]
