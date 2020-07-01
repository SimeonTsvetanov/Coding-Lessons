// Judge: 05. Check for Symmetry - https://judge.softuni.bg/Contests/Practice/Index/307#4
let expect = require('chai').expect;
let isSymmetric = require('../02. Check for Symmetry').isSymmetric;

describe('isSymmetric tests for check for symmetry of an array', function () {
    it('should return false if array is not array', function () {
        const input = 'not array';
        const result = isSymmetric(input);
        expect(result).to.be.false;
    });

    it('should return false if array is not symmetric', function () {
        const input = [1, 2, 3];
        const result = isSymmetric(input);
        expect(result).to.be.false;
    });

    it('should be true if array input is symmetric', function () {
        const input = [1, 1, 1];
        const result = isSymmetric(input);
        expect(result).to.be.true;
    });

    it("should return true for [1]", function () {
        expect(isSymmetric([1])).to.be.equal(true);
    });

    it("should return false for [1, 2]", function () {
        expect(isSymmetric([1])).to.be.equal(true);
    });

    it("should return true for [5,'hi',{a:5},new Date(),{a:5},'hi',5]", function () {
        expect(isSymmetric([5,'hi',{a:5},new Date(),{a:5},'hi',5])).to.be.equal(true);
    });
});