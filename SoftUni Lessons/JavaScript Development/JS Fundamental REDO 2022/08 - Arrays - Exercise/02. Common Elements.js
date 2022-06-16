function commonElements (arr1, arr2) {
    // MasK
    arr1.forEach(element => {
        if (arr2.includes(element)) {
            console.log(element);
        }
    });
}

commonElements(['Hey', 'hello', 2, 4, 'Peter', 'e'],
    ['Petar', 10, 'hey', 4, 'hello', '2']
);