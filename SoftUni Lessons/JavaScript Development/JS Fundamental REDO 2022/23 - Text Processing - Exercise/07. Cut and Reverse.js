function cutAndReverse (string) {
    // MasK
    let middle = string.length / 2;
    let firstHalf = string.slice(0, middle).split('').reverse().join('');
    let secondHalf = string.slice(middle, string.length).split('').reverse().join('');
    console.log(firstHalf);
    console.log(secondHalf);
}

cutAndReverse('tluciffiDsIsihTgnizamAoSsIsihT');
// ThisIsDifficult
// ThisIsSoAmazing
