function hospital(input) {
    // Mask
    let totalDays = Number(input.shift());

    let docs = 7;  
    let fixed = 0;  // :D
    let broken = 0;  // :D

    for(let day = 1; day <= totalDays; day += 1) {
        if (day % 3 === 0 && broken > fixed) {
            docs += 1;
        }

        patients = Number(input.shift());
        if (patients <= docs) {
            fixed += patients;
        } else {
            broken += patients - docs;
            fixed += docs;
        }
    }

    console.log(`Treated patients: ${fixed}.`);
    console.log(`Untreated patients: ${broken}.`); 
}

hospital([4, 7, 27, 9, 1]);  // Should return:
// Treated patients: 23.
// Untreated patients: 21.

hospital([6, 25, 25, 25, 25, 25, 2]);  // Should return:
// Treated patients: 40.
// Untreated patients: 87.