function oddOccurrences (data) {
    // MasK
    let result = [];
    data = data.split(' ')
    data.forEach(word => {
        let count = data.filter(x => x.toLowerCase() === word.toLowerCase()).length;
        if ((!result.includes(word.toLowerCase())) && count % 2 !== 0) {
            result.push(word.toLowerCase())
        }
    });
    console.log(...result);
}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
// c# php 1 5

console.log();

oddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');
// soft food