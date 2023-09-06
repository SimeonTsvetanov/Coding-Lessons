function mask (yyyy, mm, dd) {
    // MASK

    let d = new Date(yyyy, mm - 1, dd);
    d.setDate(d.getDate() + 1);
    console.log([d.getFullYear(), (d.getMonth() + 1).toString(), d.getDate().toString()].join('-'));
}

mask(2016, 9, 30 );
//

mask(2020, 3, 24);
//
