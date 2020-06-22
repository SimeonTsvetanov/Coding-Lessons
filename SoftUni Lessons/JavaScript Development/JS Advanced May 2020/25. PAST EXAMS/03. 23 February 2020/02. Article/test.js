array = [{id: 1, username: 'x'}, {id: 2, username: 'a'}, {id: 3, username: 'c'}];

sorting = {
    'asc': (a, b) => a.id - b.id,
    'desc': (a, b) => b.id - a.id,
    'username': (a, b) => a.username.localeCompare(b.username),
};

let sortingType = 'username';
sortingType = sorting[sortingType];

let b = array.sort(sortingType);
console.log(b);
