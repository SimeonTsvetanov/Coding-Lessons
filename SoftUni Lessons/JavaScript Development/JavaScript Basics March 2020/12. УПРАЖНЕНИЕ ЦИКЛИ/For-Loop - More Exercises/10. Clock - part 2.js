function clock2(input) {
    // Mask
    for (hour = 0; hour <= 23; hour++) {
        for (minute = 0; minute <= 59; minute++) {
            for (second = 0; second <= 59; second++) {
                console.log(`${hour} : ${minute} : ${second}`);
            }
        }
    }
}

clock2();  // Should return:
// 0 : 0 : 0
// 0 : 0 : 1
// 0 : 0 : 2
// 0 : 0 : 3
// 0 : 0 : 4
// 0 : 0 : 5
// 0 : 0 : 6
// 0 : 0 : 7
// 0 : 0 : 8
// 0 : 0 : 9
// 0 : 0 : 10
// ...
// 23 : 59 : 50
// 23 : 59 : 51
// 23 : 59 : 52
// 23 : 59 : 53
// 23 : 59 : 54
// 23 : 59 : 55
// 23 : 59 : 56
// 23 : 59 : 57
// 23 : 59 : 58
// 23 : 59 : 59
