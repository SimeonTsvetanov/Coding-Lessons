function orderRectangle(pairs) {
    // This is from work at home:
    /*
        let rectangles = [];

    pairs.map(pair => {
        let rectangle = {
            width: pair[0],
            height: pair[1],
            area: function() { return this.width * this.height },
            compareTo: function(other) { return other.area() - this.area() || other.width - this.width },
        };
        rectangles.push(rectangle);
    });

    rectangles = rectangles.sort((a, b) => {
        return a.compareTo(b);
    });

    return rectangles;
    */

    // And this is from work in class:
    const template = {
        width: 0,
        height: 0,
        area: function() { return this.width * this.height },
        compareTo: function(other) { return other.area() - this.area() || other.width - this.width },
    };

    return pairs
        .map(([width, height]) =>
            Object.assign(Object.create(template), { width, height })
        )
        .sort((a, b) => a.compareTo(b));
}

console.log(orderRectangle([[10,5],[5,12]]));
// Should Return:
/*
[{width:5, height:12, area:function(), compareTo:function(other)},
{width:10, height:5, area:function(),compareTo:function(other)}]
 */

console.log(orderRectangle([[10,5], [3,20], [5,12]]));
// Should Return:
/*
[{width:5, height:12, area:function(), compareTo:function(other)},
{width:3, height:20, area:function(),compareTo:function(other)},
{width:10, height:5, area:function(),compareTo:function(other)}]]
 */

