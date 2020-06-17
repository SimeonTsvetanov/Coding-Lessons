function cars(input) {
    let objects = {};

    input.map(data => {
        data = data.split(' ');
        data[0] === 'create' && data.length === 2 ? create(data[1]) : 'ass';
        data[0] === 'create' && data.length === 4 ? createAndInherit(data[1], data[3]) : 'pass';
        data[0] === 'set' ? set(data[1], data[2], data[3]) : 'or';
        data[0] === 'print' ? print(data[1]) : 'gas';
    });

    function create(name) {
        objects[name] = {};
    }

    function createAndInherit(name, parentName) {
        let parent = objects[parentName];
        objects[name] = Object.create(parent);
    }

    function set(name, key, value) {
        objects[name][key] = value;
    }

    function print(name) {
        let items = [];
        // We need to use FOR IN or it won't get the parent attributes...
        for (let i in objects[name]) {
            items.push(`${i}:${objects[name][i]}`);
        }
        console.log(items.join(', '));
    }
}

cars(['create c1',
    'create c2 inherit c1',
    'set c1 color red',
    'set c2 model new',
    'print c1',
    'print c2']
);
// Expected Output:
// color:red
// model:new, color:red
