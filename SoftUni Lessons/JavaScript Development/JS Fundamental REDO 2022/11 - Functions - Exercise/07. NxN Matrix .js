function nByN (n) {
    // MasK
    let matrix = new Array(n).fill(new Array(n).fill(n))
    console.log(matrix.map(row => row.join(" ")).join("\n"));
}

nByN(7);