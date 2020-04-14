function foreignLanguages(country) {
    // Mask
    if (country == "England" || country == "USA") {
        console.log("English");
    } else if (country == "Spain" || country == "Argentina" || country == "Mexico") {
        console.log("Spanish");
    } else {
        console.log('unknown');
    }
}

foreignLanguages('USA');  // Should return: English

foreignLanguages('Germany');  // Should return: unknown