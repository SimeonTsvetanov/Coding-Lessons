// Test in Judge -> https://judge.softuni.bg/Contests/Practice/Index/335#3

let expect = require('chai').expect;
let mathEnforcer = require('../03. Math Enforcer').mathEnforcer;


describe(`testing mathEnforced functionality and all it's sub functions`, function () {
    // taddFive(number):
    describe('testing the taddFive function', function () {
        it('should return undefined if the argument not a number', function () {
            expect(mathEnforcer.addFive('not a number')).to.equal(undefined);
        });
        it('should return the number given as an argument + 5', function () {
            expect(mathEnforcer.addFive(64)).to.equal(69);                             // <--Positive
            expect(mathEnforcer.addFive(-5)).to.be.equal(0);                           // <--Negative
            expect(mathEnforcer.addFive(64.69)).to.be.closeTo(69.69, 0.01);    // <--Floating Point
        });
    });
    // subtractTen(number):
    describe('testing the subtractTen function', function () {
        it('should return undefined if the argument not a number', function () {
            expect(mathEnforcer.subtractTen('not a number')).to.equal(undefined);
        });
        it('should return the number given as an argument - 10', function () {
            expect(mathEnforcer.subtractTen(79)).to.equal(69);                          // <--Positive
            expect(mathEnforcer.subtractTen(-59)).to.be.equal(-69);                     // <--Negative
            expect(mathEnforcer.subtractTen(79.69)).to.be.closeTo(69.69, 0.01); // <--Floating Point
        });
    });
    // sum(numOne, numTwo):
    describe('testing the sum function', function () {
        it('should return undefined if any of the two arguments is not a number', function () {
            expect(mathEnforcer.sum('not a number', 69)).to.equal(undefined);
            expect(mathEnforcer.sum(69,'not a number')).to.equal(undefined);
            expect(mathEnforcer.sum('sixty nine','not a number')).to.equal(undefined);
        });
        it('should return undefined if only one number is given', function () {
            expect(mathEnforcer.sum(69)).to.equal(undefined);
        });
        it('should return the sum of the two numbers if everything is right.', function () {
            expect(mathEnforcer.sum(60, 9)).to.equal(69);
            expect(mathEnforcer.sum(-70, 1)).to.equal(-69);
            expect(mathEnforcer.sum(60.69, 9)).to.equal(69.69);
            expect(mathEnforcer.sum(2.7, 3.4)).to.be.closeTo(6.1, 0.01);
        });
    });
});