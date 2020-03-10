function metricConverter(input) {    
    let mesure = Number(input.shift());
    let from = input.shift();
    let to = input.shift();

    let formula = `${from}/${to}`;

    calculatiоn = {
        'm/mm': 1000,
        'm/cm': 100,
        'cm/m': 0.01,
        'cm/mm': 10,
        'mm/m': 0.001,
        'mm/cm': 0.1
    };
    
    let result = mesure * calculatiоn[formula];
    console.log(result.toFixed(3));
}

metricConverter(["12", "mm", "m"]);  // Expexted output: 0.012
metricConverter(["150", "m", "cm"]);  // Expexted output: 15000.000
metricConverter(["45", "cm", "mm"]);  // Expexted output: 450.000
