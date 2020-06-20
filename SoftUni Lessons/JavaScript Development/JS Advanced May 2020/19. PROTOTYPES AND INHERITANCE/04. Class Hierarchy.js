function hierarchy() {
    // Write a function that returns 3 classes - Figure, Circle and Rectangle.

    class Figure {
        // Should have property units ("m", "cm", "mm") with default value "cm"
        // Has method changeUnits that sets different units for that figure
        constructor(units = 'cm') {
            this.units = units;
        }
        changeUnits(newUnits) {
            this.units = newUnits;
        }
        get area() {
            throw new Error('Not implemented!')
        }

        transformMetric(valInCm) {
            return this.units === 'm' ?
            valInCm / 100 : this.units === 'mm' ? valInCm * 10 : valInCm;
        }
    }

    class Circle extends Figure {
        // Extends Figure
        // Has a property radius
        // Overrides area getter to return the area of the Circle (PI * r * r)
        // toString() - should return a string representation of the figure in the format
        // "Figures units: {type} Area: {area} - radius: {radius}"
        constructor(radius, units) {
            super(units);
            this.radius = radius;
        }
        get area() {
            const radius = this.transformMetric(this.radius);
            return Math.PI * radius * radius;
        }

        toString() {
            const r = this.transformMetric(this.radius);
            return `Figures units: ${this.units} Area: ${this.area} - radius: ${r}`;
        }
    }

    class Rectangle extends Figure {
        // Extends Figure
        // Has properties width and height
        // Overrides area getter to return the area of the Rectangle (width * height)
        // toString() - should return a string representation of the figure in the format
        // Figures units: {type} Area: {area} - width: {width}, height: {height}"
        constructor(width, height, units) {
            super(units);
            this.width = width;
            this.height = height;
        }

        get area() {
            const width = this.transformMetric(this.width);
            const height = this.transformMetric(this.height);
            return width * height;
        }

        toString() {
            const w = this.transformMetric(this.width);
            const h = this.transformMetric(this.height);
            return `Figures units: ${this.units} Area: ${this.area} - width: ${w}, height: ${h}`;
        }
    }

    return {
        // Your function should return an object containing the Figure, Circle and Rectangle classes.
        Figure,
        Circle,
        Rectangle,
    };
}

hierarchy();