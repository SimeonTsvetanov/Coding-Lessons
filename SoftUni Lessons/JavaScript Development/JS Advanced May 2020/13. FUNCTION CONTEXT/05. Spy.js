// Stupid naming,... 
// Class name should be with small letters!!!

function Spy(obj, methodName) {
    const spy = { count: 0 };
    const method = obj[methodName];
    if (!method)  { throw new Error('No such method'); }
    // Here we can say spy.count ++ instead of all that:
    obj[methodName] = function (...args) {
        this.count ++;
        return method.apply(obj, args);
    }.bind(spy);
    return spy;
}

const obj = {test: function () { return 1; } };
const s = Spy(obj, 'test');
obj.test(); // { count: 1 }
obj.test(); // { count: 2 }
obj.test(); // { count: 3 }
console.log(s);
