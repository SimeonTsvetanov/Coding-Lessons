function mask (...params) {
    // MASK
    const [pages, pagerPerHour, days] = params;
    console.log(pages / pagerPerHour / days);
}

mask(212,
20 ,
2);
// 5.3

mask(432,
15 ,
4);
// 7.2
