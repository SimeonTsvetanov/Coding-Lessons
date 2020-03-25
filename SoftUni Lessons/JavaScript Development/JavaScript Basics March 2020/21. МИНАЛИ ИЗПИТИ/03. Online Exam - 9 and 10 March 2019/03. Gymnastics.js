function gymnastics(params) {
    let country = params.shift();
    let tool = params.shift();

    let scores = {
        'Russia': {'ribbon': 9.100 + 9.400, 'hoop': 9.300 + 9.800, rope: 9.600 + 9.000},
        'Bulgaria': {'ribbon': 9.600 + 9.400, 'hoop': 9.550 + 9.750, rope: 9.500 + 9.400},
        'Italy': {'ribbon': 9.200 + 9.500, 'hoop': 9.450 + 9.350, rope: 9.700 + 9.150}
    };

    let score = scores[country][tool];
    let percentage = ((20 - score) / 20) * 100;

    console.log(`The team of ${country} get ${score.toFixed(3)} on ${tool}.`);
    console.log(`${percentage.toFixed(2)}%`);
}


gymnastics(['Bulgaria', 'ribbon']);  // Expected output:
// The team of Bulgaria get 19.000 on ribbon.
// 5.00%

gymnastics(['Russia', 'rope']);  // Expected output:
// The team of Russia get 18.600 on rope.
// 7.00%

gymnastics(['Italy', 'hoop']);  // Expected output:
// The team of Italy get 18.800 on hoop.
// 6.00%
