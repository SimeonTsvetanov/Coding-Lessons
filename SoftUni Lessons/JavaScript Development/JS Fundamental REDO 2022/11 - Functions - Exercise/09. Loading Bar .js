function loadingBar (percent) {
    // MasK
    let filling = percent / 10;
    let bar = new Array(filling).fill('%').concat(new Array(10 - filling).fill('.'))
    let print = `[${bar.join('')}]`;

    if (percent === 100) {
        console.log(`100% Complete!`);
        console.log(print);
    } else {
        console.log(`${percent}% ${print}`);
        console.log(`Still loading...`);
    }
}

loadingBar(30);  // 30% [%%%.......]