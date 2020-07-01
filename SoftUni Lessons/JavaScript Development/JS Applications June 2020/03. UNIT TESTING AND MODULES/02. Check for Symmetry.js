// Judge: 05. Check for Symmetry - https://judge.softuni.bg/Contests/Practice/Index/307#4

function isSymmetric(arr) {
    if (!Array.isArray(arr))
        return false; // Non-arrays are non-symmetric
    let reversed = arr.slice(0).reverse(); // Clone and reverse
    let equal = (JSON.stringify(arr) == JSON.stringify(reversed));
    return equal;
}
module.exports = { isSymmetric };