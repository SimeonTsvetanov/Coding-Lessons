function spiceMustFlow(input) {
    // Mask
    // This task if fuc***g stupid. The Description is pointless... adn wrong!

    let source = Number(input);
    let extracted = 0;
    let days = 0;
    if (source < 100) {
        console.log(days);
        console.log(extracted);
    } else {
        while (source >= 100) {
            days += 1;
            extracted += source - 26;
            source -= 10;
        }
        console.log(days);
        console.log(extracted - 26);
    }
}

spiceMustFlow(111);  // Should return:
// 2
// 134
