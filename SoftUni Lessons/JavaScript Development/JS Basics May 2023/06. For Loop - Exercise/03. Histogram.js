function histogram(params) {
    let groups = {
        0: [],  // < 200
        1: [],  // 200 … 399
        2: [],  // 400 … 599
        3: [],  // 600 … 799
        4: [],  // ≥ 800
    }
    
    let numbers = params.slice(1, params.length).map(Number);
    let count = numbers.length;

    numbers.forEach(num => {
        if (num < 200) {
            groups[0].push(num);
        } else if (num >= 200 && num <= 399) {
            groups[1].push(num);
        } else if (num >=400 && num <= 599) {
            groups[2].push(num);
        } else if (num >= 600 && num <= 799) {
            groups[3].push(num);
        } else {
            groups[4].push(num);
        }
    });

    for (let i = 0; i < 5; i++) {
        console.log(`${(groups[i].length / count * 100).toFixed(2)}%`);
    }
}

histogram(["3",
"1",
"2",
"999"]);

// 66.67%
// 0.00%
// 0.00%
// 0.00%
// 33.33%

histogram(["7",
"800",
"801",
"250",
"199",
"399",
"599",
"799"]);

// 14.29%
// 28.57%
// 14.29%
// 14.29%
// 28.57%

