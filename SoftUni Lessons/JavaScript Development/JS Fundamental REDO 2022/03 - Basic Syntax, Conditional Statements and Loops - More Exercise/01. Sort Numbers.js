function sortNumbers(a, b, c) {
    console.log([a, b, c].sort((a, b) => b - a).join('\n'));
}

sortNumbers(2, 1, 3);
sortNumbers(-2, 1, 3);