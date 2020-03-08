function fishland(input) {
    let pricePalamudKg = Number(input.shift());
    let priceSafridKg = Number(input.shift());
    let KgPalamud = Number(input.shift());
    let kgSafrid = Number(input.shift());
    let kgMidi = Number(input.shift());

    let palamudFor1Kg = pricePalamudKg + (pricePalamudKg * 0.60);
    let palamudTotal = palamudFor1Kg * KgPalamud;
    let safridFor1Kg = priceSafridKg + (priceSafridKg *0.80);
    let safridTotal = safridFor1Kg * kgSafrid; 
    let midiTotal = kgMidi * 7.50;

    let total = (palamudTotal + safridTotal + midiTotal).toFixed(2);
    console.log(total);
}

fishland([6.90, 4.20, 1.5, 2.5, 1]) // Expected output: 42.96
fishland([5.55, 3.57, 4.3, 3.6, 7]) // Expected output: 113.82
fishland([7.79, 5.35, 9.3, 0, 0]) // Expected output: 115.92