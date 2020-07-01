// Test in Judge -> https://judge.softuni.bg/Contests/Practice/Index/756#1

let expect = require('chai').expect;
let StringBuilder = require('../05. String Builder').StringBuilder;

describe('StringBuilder', function () {
    let build;

    describe('with empty constructor', function () {
        beforeEach(function () {
            build = new StringBuilder();
        });

        it('has all properties', function () {
            expect(build.hasOwnProperty('_stringArray')).to.equal(true, "Missing _stringArray property");
        });

        it('has functions attached to prototype', function () {
            expect(Object.getPrototypeOf(build).hasOwnProperty('append')).to.equal(true);
            expect(Object.getPrototypeOf(build).hasOwnProperty('prepend')).to.equal(true);
            expect(Object.getPrototypeOf(build).hasOwnProperty('insertAt')).to.equal(true);
            expect(Object.getPrototypeOf(build).hasOwnProperty('remove')).to.equal(true);
            expect(Object.getPrototypeOf(build).hasOwnProperty('toString')).to.equal(true);
        });

        it('must initialize data to an empty array', function () {
            expect(build._stringArray instanceof Array).to.equal(true);
            expect(build._stringArray.length).to.equal(0);
        });
    });

    it('initialization does not throw', function () {
        let initEmpty = () => build = new StringBuilder();
        expect(initEmpty).to.not.throw();
        let initParam = () => build = new StringBuilder('hello');
        expect(initParam).to.not.throw();
    });

    it('invalid constructor parameter', function () {
        let willThrow = () => build = new StringBuilder(5);
        expect(willThrow).to.throw();
    });

    describe('constructor with parameter', function () {
        let startingString = 'hello';

        beforeEach(function () {
            build = new StringBuilder(startingString);
        });

        it('must initialize data to a string array', function () {
            expect(build._stringArray instanceof Array).to.equal(true, 'Data must be of type array');
            compareArray(build._stringArray, Array.from(startingString));
        });

        it('appends correctly', function () {
            let str = ', world';
            build.append(str);
            compareArray(build._stringArray, Array.from(startingString + str));
        });

        it('prepends correctly', function () {
            let str = 'welcome ';
            build.prepend(str);
            compareArray(build._stringArray, Array.from(str + startingString));
        });

        it('inserts correctly', function () {
            let str = 'kek';
            build.insertAt(str, 3);
            let expected = Array.from(startingString);
            expected.splice(3, 0, ...str);
            compareArray(build._stringArray, expected);
        });

        it('removes correctly', function () {
            build.remove(1, 3);
            compareArray(build._stringArray, Array.from('ho'));
        });

        it('stringifies correctly', function () {
            expect(build.toString()).to.equal(startingString);
        });

        it('invalid append parameter', function () {
            let willThrow = () => build.append(5);
            expect(willThrow).to.throw();
        });

        it('invalid prepend parameter', function () {
            let willThrow = () => build.prepend(5);
            expect(willThrow).to.throw();
        });

        it('invalid insertAt parameter', function () {
            let willThrow = () => build.insertAt(5, 1);
            expect(willThrow).to.throw();
        });
    });

    function compareArray(source, expected) {
        expect(source.length).to.equal(expected.length, "Arrays don't match");
        for (let i = 0; i < source.length; i++) {
            expect(source[i]).to.equal(expected[i], 'Element ' + i + ' mismatch');
        }
    }
});