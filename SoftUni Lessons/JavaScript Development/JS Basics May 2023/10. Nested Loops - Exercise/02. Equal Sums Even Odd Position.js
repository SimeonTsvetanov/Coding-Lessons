function solution(params) {
    // MasK
    let start = Number(params.shift());
    let end = Number(params.shift());

    let result = [];

    for(let num = start; num <= end; num++) {
        let sumEqual = 0;
        let sumOdd = 0;

        for (let i = 1; i <= String(num).length; i++) {
            let j = Number(String(num)[i - 1]);
            (i % 2 == 0) ? sumEqual += j : sumOdd += j;
        }

        (sumEqual === sumOdd) ? result.push(num) : 'pass';
    }

    console.log(result.join(' '));
}

solution(["100000",
"100050"]);

// 100001 100012 100023 100034 100045

console.log('********************************');

solution(["123456",
"124000"]);

// 123464 123475 123486 123497 123530 123541 123552 123563 123574 123585 123596 123640 123651 123662 123673 123684 123695 123750 123761 123772 123783 123794 123860 123871 123882 123893 123970 123981 123992