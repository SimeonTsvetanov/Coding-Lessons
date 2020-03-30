function clock(input) {
    // Mask
    for (hour = 0; hour <= 23; hour++) {
        for (minute = 0; minute <= 59; minute++) {
            console.log(`${hour} : ${minute}`);
            
        }
    }
}

clock();  // Should return:
// 0 : 0
// 0 : 1
// 0 : 2
// 0 : 3
// 0 : 4
// 0 : 5
// 0 : 6
// 0 : 7
// 0 : 8
// 0 : 9
// 0 : 10
// ...
// 23 : 50
// 23 : 51
// 23 : 52
// 23 : 53
// 23 : 54
// 23 : 55
// 23 : 56
// 23 : 57
// 23 : 58
// 23 : 59

