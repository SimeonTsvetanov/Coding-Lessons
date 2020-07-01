// Test in Judge -> https://judge.softuni.bg/Contests/Practice/Index/335#2

let expect = require('chai').expect;
let lookupChar = require('../02. Char Lookup').lookupChar;

describe('testing lookupChar function', function () {
    // Bad cases:
    describe('testing the bad cases', function () {
        it('should return undefined with the first argument is empty string', function () {
            expect(lookupChar(69, 69)).to.equal(undefined);
        });
        it('should return undefined with the first argument is floating point', function () {
            expect(lookupChar('string', 69.69)).to.equal(undefined);
        });
        it('should return undefined with the second argument is a string', function () {
            expect(lookupChar('string', 'sixty nine')).to.equal(undefined);
        });
        it('should return "Incorrect index" message if the index is below zero or bigger than the string length',
            function () {
            expect(lookupChar('string', -69)).to.equal("Incorrect index");
            expect(lookupChar('string', 69)).to.equal("Incorrect index");
        });
    });
    // Happy ending Cases:------------------------------------------------------------- not that happy end... horny ass!
    describe('testing the good cases', function () {
        it('should return: "g" if all the arguments are valid', function () {
            expect(lookupChar('string', 5)).to.equal('g');
        });
    });
});