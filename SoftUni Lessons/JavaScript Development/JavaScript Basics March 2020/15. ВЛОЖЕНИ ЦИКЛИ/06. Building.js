function building(input) {
    // Mask
    let levels = Number(input.shift());
    let rooms = Number(input.shift());

    let type = undefined;

    for (let level = levels; level > 0; level--) {
        let floor = ''

        for (let room = 0; room < rooms; room++) {
            if (level == levels) {type = "L";}
            else if (level % 2 == 0) {type = "O";}
            else if (level % 2 != 0) {type = "A";}

            floor += `${type}${level}${room} `;
        }
        console.log(floor);
    }
}

building([6, 4]);  // Should return:
// L60 L61 L62 L63
// A50 A51 A52 A53
// O40 O41 O42 O43
// A30 A31 A32 A33
// O20 O21 O22 O23
// A10 A11 A12 A13


building([9, 5]);  // Should return:
// L90 L91 L92 L93 L94
// O80 O81 O82 O83 O84
// A70 A71 A72 A73 A74
